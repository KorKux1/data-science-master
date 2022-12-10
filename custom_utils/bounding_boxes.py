"""
We take the structure of the dataset to load the images and the bouding boxes.
"""
import torch
from torch.utils.data import Dataset
import cv2
import pandas as pd
import typing as ty
from numpy.typing import NDArray
import numpy as np
from skimage import io
import os


transform_func_inp_signature = ty.Dict[str, NDArray[np.float_]]

transform_func_signature = ty.Callable[
    [transform_func_inp_signature],
    transform_func_inp_signature
]

class MNISTDataset(Dataset):
    """
    Location MNIST dataset.

    This class is used to load the MNIST dataset and to apply the transformations to the images.

    Source: https://www.kaggle.com/code/sebastingarcaacosta/tutoria-1
    
    Args:
        df (pandas.DataFrame): DataFrame with the data.
        root_dir (string): Root directory of dataset where directory
            ``train`` and  ``test`` exist.
        labeled (bool): If True, the dataset is labeled.
        transform (callable, optional): A function/transform that  takes in an PIL image
            and returns a transformed version.
    """
    def __init__(
        self, 
        df: pd.DataFrame, 
        root_dir: str, 
        labeled: bool = True,
        transform: ty.Optional[ty.List[transform_func_signature]] = None,
        gray: bool = False
    ) -> None:
        self.df = df
        self.root_dir = root_dir
        self.transform = transform
        self.labeled = labeled
        self.gray = gray
        
    def __len__(self):
        return self.df.shape[0]
    
    def __getitem__(self, idx: int) -> transform_func_signature: 
        if torch.is_tensor(idx):
            idx = idx.tolist()
        
        # Read image
        img_name = os.path.join(self.root_dir, self.df.filename.iloc[idx])
        image = io.imread(img_name)
        
        # Convert from gray to RGB
        if not self.gray:
            image = cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)

        sample = {'image': image}
        
        if self.labeled:
            # Read labels
            img_class = self.df.class_id.iloc[idx]
            img_bbox = self.df.iloc[idx, 2:]

            img_bbox = np.array([img_bbox]).astype('float')
            img_class = np.array([img_class]).astype('int')
            sample.update({'bbox': img_bbox, 'class_id': img_class})
        
        if self.transform:
            sample = self.transform(sample)
        
        return sample

def normalize_bbox(bbox, factor: int = 100):
    """
    Normalize the bounding box.

    Source: https://www.kaggle.com/code/sebastingarcaacosta/tutoria-1

    Args:
        bbox (list): List of bouding boxes.
        factor (int): Factor to normalize the bounding box.

    Returns:
        bbox (list): List of normalized bouding boxes.
    """
    return list(map(lambda x: int(x * factor), bbox))


def draw_classes(imgs, classes, colors, origin, offset: int = 5, prefix: str =''):
    """
    Draw the classes on the images.

    Source: https://www.kaggle.com/code/sebastingarcaacosta/tutoria-1

    Args:
        imgs (list): List of images.
        classes (list): List of classes.
        colors (list): List of colors.
        origin (list): List of origins.
        offset (int): Offset.
        prefix (str): Prefix.

    Returns:
        imgs (list): List of images with the classes.
    """
    for i, (img, class_id, color) in enumerate(zip(imgs, classes, colors)):        
        imgs[i] = cv2.putText(
            img, f'{prefix}{class_id.squeeze()}', 
            origin, cv2.FONT_HERSHEY_SIMPLEX, 
            0.4, color, 1, cv2.LINE_AA
        )
    return imgs


def draw_bbox(img, bbox, color):
    """
    Draw the bounding box on the image.

    Source: https://www.kaggle.com/code/sebastingarcaacosta/tutoria-1

    Args:
        img (list): List of images.
        bbox (list): List of bouding boxes.
        color (list): List of colors.

    Returns:
        img (list): List of images with the bounding box.
    """
    xmin, ymin, xmax, ymax = bbox
    img = cv2.rectangle(img, (xmin, ymin), (xmax, ymax), color, 2)
    return img


def draw_bboxes(imgs, bboxes, colors):
    """
    Draw bounding boxes on images.

    Source: https://www.kaggle.com/code/sebastingarcaacosta/tutoria-1

    Args:
        imgs (torch.Tensor): Images.
        bboxes (torch.Tensor): Bounding boxes.
        colors (list): List of colors.
    
    Returns:
        torch.Tensor: Images with bounding boxes.
    """
    for i, (img, bbox, color) in enumerate(zip(imgs, bboxes, colors)):
        imgs[i] = draw_bbox(img, bbox, color)
    return imgs


def draw_predictions(imgs, classes, bboxes, colors, origin):
    """
    Draw the predictions on the images.

    Source: https://www.kaggle.com/code/sebastingarcaacosta/tutoria-1

    Args:
        imgs (list): List of images.
        classes (list): List of classes.
        bboxes (list): List of bouding boxes.
        colors (list): List of colors.
        origin (list): List of origins.
    
    Returns:
        imgs (list): List of images with the predictions.
    """
    assert all(len(x) > 0 for x in [imgs, classes, bboxes, colors])
    if len(colors) == 1:
        colors = [colors[0] for _ in imgs]
    imgs = draw_bboxes(imgs, bboxes, colors)
    imgs = draw_classes(imgs, classes, colors, origin)
    return imgs