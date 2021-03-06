# Vehicle-speed-and-congestion-detector

---

***The [TensorFlow Object Detection API]("https://github.com/tensorflow/models/tree/master/research/object_detection") is used as a base for object counting on this project, more info can be found on this [repo](https://github.com/nins15/Vehicle-speed-and-congestion-detector/tree/master/utils). Apart from that some code is also based on this [site](https://pythonprogramming.net/introduction-use-tensorflow-object-detection-api-tutorial/)***

---


* Objects like car ,truck and person are detected using Tensorflow object detection api
* Speed is calculated for the last dtected object along with its directio
* If any two objects come too close to each other then "WARNING" is displayed to mark congestion

---

<p align="center">
  <img src="https://github.com/nins15/Vehicle-speed-and-congestion-detector/blob/master/images/Forgif.gif">
</p>

---

## Model Architecture


<p align="center">
  <img src="https://github.com/nins15/Vehicle-speed-and-congestion-detector/blob/master/images/Modelarchitecture.png">
</p>

## Model used : FasterRCNN
<p align="center">
  <img src="https://github.com/nins15/Vehicle-speed-and-congestion-detector/blob/master/images/fasterrcnn.png">
</p>

## Congestion detection and Speed detection:

* Speed detection is done using pixel location and can be found in file [syn](https://github.com/nins15/Vehicle-speed-and-congestion-detector/blob/master/utils/syn.py)
* Congestion detection is done by calculating the centroids of two objects and if two objects come too close to each other then "WARNING" sign is diplayed
