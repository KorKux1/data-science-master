import typing as ty
import torch

from bounding_boxes import MNISTDataset

from torch import nn
from torch import Tensor
from torchvision import ops
from torch.nn import CrossEntropyLoss
from torch.optim import Optimizer
from torch.utils.data import DataLoader


class FeatureExtractor(nn.Module):
    """Feature extractor for the model."""
    
    def __init__(self, channels: int):
        super().__init__()
        # Arquitecture: 784 (gray) - [32C3-32C3-32C5S2] - [64C3-64C3-64C5S2] - [128C3-128C3-128C5S2] - 128 - 10 (classification)
        # Arquitecture: 784 (gray) - [32C3-32C3-32C5S2] - [64C3-64C3-64C5S2] - [128C3-128C3-128C5S2] - 768 -256 - 128 - 4 (regression)
        self.channels = channels

        self.features = nn.Sequential(
            # 3 Subsampling layers
            nn.Conv2d(self.channels, 32, kernel_size=3),
            nn.ReLU(),
            nn.BatchNorm2d(32),
            nn.Conv2d(32, 32, kernel_size=3),
            nn.ReLU(),
            nn.BatchNorm2d(32),
            nn.Conv2d(32, 32, kernel_size=5, stride=2, padding=(2, 2)),
            nn.ReLU(),
            nn.BatchNorm2d(32),
            nn.Dropout(0.4),
            nn.Conv2d(32, 64, kernel_size=3),
            nn.ReLU(),
            nn.BatchNorm2d(64),
            nn.Conv2d(64, 64, kernel_size=3),
            nn.ReLU(),
            nn.BatchNorm2d(64),
            nn.Conv2d(64, 64, kernel_size=5, stride=2, padding=(2, 2)),
            nn.ReLU(),
            nn.BatchNorm2d(64),
            nn.Dropout(0.4),
            # nn.Conv2d(64, 128, kernel_size=3),
            # nn.ReLU(),
            # nn.BatchNorm2d(128),
            # nn.Conv2d(128, 128, kernel_size=2),
            # nn.ReLU(),
            # nn.BatchNorm2d(128),
            # nn.Conv2d(128, 128, kernel_size=1, stride=2, padding=(2, 2)),
            # nn.ReLU(),
            # nn.BatchNorm2d(128),
            # nn.Dropout(0.4),
            nn.Flatten(),
        )

    def forward(self, x):
        out = self.features.forward(x)
        return out


class ClassificationHead(nn.Module):
    """Classification head for the model."""
    def __init__(self, input_size: int, n_classes: int):
        super().__init__()
        self.input_size = input_size
        self.n_classes = n_classes
        
        self.model = nn.Sequential(
            ## Model for classification of the digits in the image (10 classes) using the features extracted by the feature extractor
            ## Shape transformation: (1.024) -> (128) -> (10)
            ## with softmax activation function for the output layer
            
            nn.Linear(in_features = self.input_size, out_features=128), # Shape transformation: (1.024) -> (128)
            nn.ReLU(),
            nn.BatchNorm1d(128),
            nn.Dropout(0.4),
            nn.Linear(in_features = 128, out_features = self.n_classes), # Shape transformation: (128) -> (10)
            # nn.Softmax()
        )
    
    def forward(self, x):
        return self.model(x)


class RegressionHead(nn.Module):
    """Regression head for the model."""
    def __init__(self, input_size: int):
        super().__init__()
        self.input_size = input_size
        self.model = nn.Sequential(
            nn.Linear(self.input_size, 768),
            nn.ReLU(),
            nn.Linear(768, 256),
            nn.ReLU(),
            nn.Linear(256, 4)
        )
    
    def forward(self, x):
        return self.model(x)


def evaluate(
    logs: ty.Dict[str, ty.Any], 
    labels: ty.Dict[str, Tensor],
    preds: ty.Dict[str, Tensor],
    eval_set: str,
    metrics: ty.Dict[str, ty.Callable[[Tensor, Tensor], Tensor]],
    losses: ty.Optional[ty.Dict[str, Tensor]] = None,
) -> ty.Dict[str, ty.Any]:
    
    if losses is not None:
        for loss_name, loss_value in losses.items():
            logs[f'{eval_set}_{loss_name}'] = loss_value
    
    for task_name, label in labels.items():
        for metric_name, metric in metrics[task_name]:
            value = metric(label, preds[task_name])
            logs[f'{eval_set}_{metric_name}'] = value
            
    return logs

class Model(nn.Module):
    def __init__(self, backbone: FeatureExtractor, classifier: ClassificationHead, regressor: RegressionHead):
        super().__init__()
        self.backbone = backbone
        self.cls_head = classifier
        self.reg_head = regressor
        
    def forward(self, x):
        features = self.backbone(x)
        cls_logits = self.cls_head(features)
        pred_bbox = self.reg_head(features)
        predictions = {'bbox': pred_bbox, 'class_id': cls_logits}
        return predictions

def step(
    model: Model, 
    optimizer: Optimizer, 
    batch: MNISTDataset,
    cls_loss_fn: CrossEntropyLoss,
    bbox_loss_fn: ty.Callable[[ty.Dict[str, torch.Tensor]], torch.Tensor],
    loss_fn: ty.Callable[[ty.Dict[str, torch.Tensor]], torch.Tensor],    
    device: str,
    alpha: float,
    train: bool = False,
) -> ty.Tuple[ty.Dict[str, Tensor], ty.Dict[str, Tensor]]:


    if train:
        optimizer.zero_grad()
        
    img = batch.pop('image').to(device)

    for k in list(batch.keys()):
        batch[k] = batch[k].to(device)

    preds = model(img.float())
    losses = loss_fn(batch, preds, cls_loss_fn, bbox_loss_fn, alpha)
    final_loss = losses['loss']
    
    if train:
        final_loss.backward()
        optimizer.step()
    
    return losses, preds


def train(
    model: Model, 
    optimizer: Optimizer, 
    dataset: DataLoader,
    eval_datasets: ty.List[ty.Tuple[str, DataLoader]],
    loss_fn: ty.Callable[[ty.Dict[str, torch.Tensor]], torch.Tensor],
    metrics: ty.Dict[str, ty.Callable[[Tensor, Tensor], Tensor]],
    callbacks: ty.List[ty.Callable[[ty.Dict[ty.Any, ty.Any]], None]],
    device: str,
    train_steps: 100,
    eval_steps: 10,
    alpha_dict: dict = {'start': 0.5, 'end': 0.9, 'step': 0.01},
) -> Model:
    # Send model to device (GPU or CPU)
    model = model.to(device)
    # Loss function for classification
    cls_loss_fn = CrossEntropyLoss()
    
    # Loss function for regression
    bbox_loss_fn = lambda batch_bbox_preds, batch_bbox: torch.trace(1-ops.box_iou(batch_bbox_preds, batch_bbox))
    
    iters = 0
    iterator = iter(dataset)
    assert train_steps > eval_steps, 'Train steps should be greater than the eval steps'
    logs = dict()

    
    while iters <= train_steps:
        logs['iters'] = iters
        # Update alpha value for the loss function for each iteration
        alpha = (alpha_dict['start'] + iters * alpha_dict['step'] * alpha_dict['end']) / (1 + iters * alpha_dict['step'])
        alpha = min(alpha, alpha_dict['end'])
        logs['alpha'] = alpha
        # Train
        # Activate layers that only needed to train
        model.train()

        # Get next batch
        try:
            batch = next(iterator)
        except StopIteration:
            iterator = iter(dataset)
            batch = next(iterator)

        # Send batch to device 
        losses, preds = step(model, optimizer, batch, cls_loss_fn, bbox_loss_fn, loss_fn, device, alpha, train=True)
        logs = evaluate(logs, batch, preds, 'train', metrics, losses)
        
        # Eval every eval_steps iterations
        if iters % eval_steps == 0:        
            # Evaluate
            # Deactives layers that only needed to train
            # https://discuss.pytorch.org/t/model-eval-vs-with-torch-no-grad/19615
            model.eval()
            
            # Avoids calculating gradients in evaluation dataset. 
            with torch.no_grad():

                for name, dataset in eval_datasets:
                    for batch in dataset:
                        losses, preds = step(model, optimizer, batch, cls_loss_fn, bbox_loss_fn, loss_fn, device, alpha, train=False)            
                        logs = evaluate(logs, batch, preds, name, metrics, losses)
        

        for callback in callbacks:
            callback(logs)
        
        iters += 1
    
    output = {'model': model, 'history': logs}

    return output