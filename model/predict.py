from model.model import Yolov4

model = Yolov4(weight_path='yolov4.weights',
                   class_name_path='class_names/coco_classes.txt')

def ret_predict():
    global model
    return model.predict(r"output.jpg")

    # r"C:\Users\Filip\Desktop\pizza1.jpg"
