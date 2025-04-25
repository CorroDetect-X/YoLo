# YoLo

using ultralytics to download the model

when you train the model a new floder is created it call runs .inside runs we have another folder is called detect.

inside detect you have a folder of train it contain all result of the trainng model .. when the model is complete the training a new folder was created is called weights ,it has best.pt and last.pt which is the best models for the trainng model.

to predict make sure to load the best model

when you load the dataset from roboflow make sure to change the path of the train and test and test from the data.yml

model = YOLO("yolov9m") // the first time it will download the model to the disc
