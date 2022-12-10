def load_config():
    config_dict = {
        'img_size': 28,
        'train_images_dir': 'datasets/images/train/',
        'batch_size': 32,
        'learning_rate': 0.001,
        'num_epochs': 200,
        'num_classes': 10,
        'weight_decay': 1e-5,
        'alpha': 0.5,
        'num_channels': 1,
    }
    return config_dict