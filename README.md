# Custom training of YOLOV8 on Traffic signs detection dataset
### Goals
The objective of this project is to train and validate the YOLOV8 model from the [Ultralytics](https://ultralytics.com/) on a custom dataset

## Documentation
### Dataset description
Get the dataset here: [Traffic_sign_Detection](https://www.kaggle.com/datasets/valentynsichkar/traffic-signs-dataset-in-yolo-format)

The dataset contain 631 images in '*.jpg' format and '*.txt' files next to every image. These '*.txt' files includes the annotations of the bounding boxes in YOLO format. The images will have objects belonging to 4 classes mentioned below :

* 1. Prohibitory- This category consists of following Traffic Signs: 
 Speed limit, No overtaking, No traffic both ways, No trucks.

* 2. Danger-  This category consists of following Traffic Sings: Priority at next intersection, Danger, Bend left, Bend right, Bend, Uneven road, Slippery road, Road narrows, Construction, Traffic signal, Pedestrian crossing, School crossing, Cycles crossing, Snow, Animals.
* 3. Mandatory- This category consists of following Traffic Sings: 
Go right, Go left, Go straight, Go right or straight, Go left or straight, Keep right, Keep left, Roundabout.

* 4. Other- This category consists of following Traffic Sings: Restriction ends, Priority road, Give way, Stop, No entry.

### Installing requirements
To install all the required libraries,after cloning the repository run the following command:
    pip install -r requirements.txt

or install Ultralytics manually - see more at [Ultralytics_docs](https://docs.ultralytics.com/quickstart/)
    pip install Ultralytics
    



