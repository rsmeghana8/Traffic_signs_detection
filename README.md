# Custom training of YOLOV8 on Traffic signs detection dataset
### Goals

https://github.com/rsmeghana8/Traffic_signs_detection/assets/57563443/e1e403b4-edcd-4e25-9944-061525bea219


The objective of this project is to implement an image and video object detection classifier using transfer learning the pretrained YOLOV8 model from the [Ultralytics](https://ultralytics.com/) on a custom dataset

## Documentation
### Dataset description
Get the dataset here: [Traffic_sign_Detection](https://www.kaggle.com/datasets/valentynsichkar/traffic-signs-dataset-in-yolo-format)

The dataset contain 631 images in '*.jpg' format and '*.txt' files next to every image. These '*.txt' files includes the annotations of the bounding boxes in YOLO format. The images will have objects belonging to 4 classes mentioned below :

* 1. Prohibitory- This category consists of following Traffic Signs: 
 Speed limit, No overtaking, No traffic both ways, No trucks.

* 2. Danger-  This category consists of following Traffic Sings: Priority at next intersection, Danger, Bend left, Bend r

https://github.com/rsmeghana8/Traffic_signs_detection/assets/57563443/a5c093bb-4bb5-47ea-8bf4-60182db0a31d

ight, Bend, Uneven road, Slippery road, Road narrows, Construction, Traffic signal, Pedestrian crossing, School crossing, Cycles crossing, Snow, Animals.
* 3. Mandatory- This category consists of following Traffic Sings: 
Go right, Go left, Go straight, Go right or straight, Go left or straight, Keep right, Keep left, Roundabout.

* 4. Other- This category consists of following Traffic Sings: Restriction ends, Priority road, Give way, Stop, No entry.

### Installing requirements
To install all the dependencies,after cloning the repository run the following command:
```
    pip install -r requirements.txt
```

or install Ultralytics manually - (see more at [Ultralytics_docs] (https://docs.ultralytics.com/quickstart/) )
```
    pip install Ultralytics
```

### Prepare the data
After downloading the data, split the dataset into Train,Test,Val in the YOLOV8 data format as below-

Update the paths to these directories in 'data.yaml'

### Training
Change the hyper-parameters in the 'params.yaml' file to fine-tune and train by running 
```
    python stage_02_training.py

```
This will download a pretrained YOLOV8 model 'yolo8n.yaml' and train in on the training data and save the model weights with best validation score as well as last iteration weights in 'runs' directory along with other results with the following structure
````

runs/
└── detect/
    ├── train1/
    ├── train2/
    ├── ...
    └── tune/
        ├── best_hyperparameters.yaml
        ├── best_fitness.png
        ├── tune_results.csv
        ├── tune_scatter_plots.png
        └── weights/
            ├── last.pt
            └── best.pt
)
```
### Evaluation
To Evaluate the trained model model on test data, in 'test.yaml' give the path to test data in for the 'val' key and run
```
   python stage_03_evaluation.py
```
### Experiments and results
When trained for 100 epochs model got the following results

|      Epochs   |  Train mAP50    | Test mAP50 |
| :------------ |:---------------:| ----------:|
|       100     |      78.7       |    87.2    |

When top 10 layers were frozen, the model trained for same 100 epochs performanced very poorly

|      Epochs   |  Train mAP50    | Test mAP50 |
| :------------ |:---------------:| ----------:|
|       100     |      10.4       |    15.1    |




    



