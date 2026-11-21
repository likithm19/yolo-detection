from ultralytics import YOLO
import numpy

#load a pretrained model (recommended for training) 
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)


#predict on an image
results = model.predict(
    source=r"c:\Users\Likit\Downloads\EANOFOTO_CruiseIn-cars-_012620-039-e1586982253648.jpg",
    conf=0.25,
    show=True,
    save=True,
)
results_1=model.predict(r"pexels-orbital101studio-19927459.jpg", conf=0.25, show=True, save=True)

#display tensor array
print(results)
print(results_1)


