yolo_config = {
    # Basic
    'img_size': (416, 416, 3),
    'anchors': [12, 16, 19, 36, 40, 28, 36, 75, 76, 55, 72, 146, 142, 110, 192, 243, 459, 401],
    'strides': [8, 16, 32],
    'xyscale': [1.2, 1.1, 1.05],

    # Training
    'iou_loss_thresh': 0.5,
    'batch_size': 8,
    'num_gpu': 1,  # 2,

    # Inference
    'max_boxes': 100,
    'iou_threshold': 0.413,
    'score_threshold': 0.3,
}

food_classes = {
    "person":0,
    "bicycle":0,
    "car":0,
    "motorbike":0,
    "aeroplane":0,
    "bus":0,
    "train":0,
    "truck":0,
    "boat":0,
    "traffic light":0,
    "fire hydrant":0,
    "stop sign":0,
    "parking meter":0,
    "bench":0,
    "bird":0,
    "cat":0,
    "dog":0,
    "horse":0,
    "sheep":0,
    "cow":0,
    "elephant":0,
    "bear":0,
    "zebra":0,
    "giraffe":0,
    "backpack":0,
    "umbrella":0,
    "handbag":0,
    "tie":0,
    "suitcase":0,
    "frisbee":0,
    "skis":0,
    "snowboard":0,
    "sports ball":0,
    "kite":0,
    "baseball bat":0,
    "baseball glove":0,
    "skateboard" :0,
    "surfboard":0,
    "tennis racket":0,
    "bottle":1,
    "wine glass":1,
    "cup":0,
    "fork":0,
    "knife":0,
    "spoon":0,
    "bowl":0,
    "banana":1,
    "apple":1,
    "sandwich":1,
    "orange":1,
    "broccoli":1,
    "carrot":1,
    "hot dog":1,
    "pizza":1,
    "donut":1,
    "cake":1,
    "chair":0,
    "sofa":0,
    "pottedplant":0,
    "bed":0,
    "diningtable":0,
    "toilet":0,
    "tvmonitor":0,
    "laptop":0,
    "mouse":0,
    "remote":0,
    "keyboard":0,
    "cell phone":0,
    "microwave":0,
    "oven":0,
    "toaster":0,
    "sink":0,
    "refrigerator":0,
    "book":0,
    "clock":0,
    "vase":0,
    "scissors":0,
    "teddy bear":0,
    "hair drier":0,
    "toothbrush":0
}