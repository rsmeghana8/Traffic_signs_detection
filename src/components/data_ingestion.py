import os
from src import logger
from random import choice
import shutil
from src.utils.common import read_yaml,create_directories
from src.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config : DataIngestionConfig):
        self.config=config


    def prepare_data(self):

        imgs = []
        labels = []

        for (dirname, dirs, files) in os.walk(self.config.source_dir):
            for filename in files:
                if filename.endswith(".txt"):
                    labels.append(filename)
                else:
                    imgs.append(filename)


        #Creating images and label directories for Train, val and test
        if not os.path.isdir(self.config.train_images):
            create_directories([self.config.train_images])

        if not os.path.isdir(self.config.train_labels):
            create_directories([self.config.train_labels])

        if not os.path.isdir(self.config.test_images):
            create_directories([self.config.test_images])

        if not os.path.isdir(self.config.test_labels):
            create_directories([self.config.test_labels])


        if not os.path.isdir(self.config.val_images):
            create_directories([self.config.val_images])

        if not os.path.isdir(self.config.val_labels):
            create_directories([self.config.val_labels])

        test_count = int(self.config.train_test_split * len(imgs))
        val_count = int(self.config.train_val_split * len(imgs))
        train_count = int(len(imgs) - test_count - val_count)
        print(len(imgs),test_count, val_count, train_count)


        for i in range(train_count):
            file_jpg = choice(imgs)
            file_txt= file_jpg[:-4]+".txt"

            shutil.copy(os.path.join(self.config.source_dir,file_jpg), os.path.join(self.config.train_images,file_jpg))
            shutil.copy(os.path.join(self.config.source_dir,file_txt), os.path.join(self.config.train_labels,file_txt))

            imgs.remove(file_jpg)
            labels.remove(file_txt)


        for i in range(val_count):
            file_jpg = choice(imgs)
            file_txt= file_jpg[:-4]+".txt"

            shutil.copy(os.path.join(self.config.source_dir,file_jpg), os.path.join(self.config.val_images,file_jpg))
            shutil.copy(os.path.join(self.config.source_dir,file_txt), os.path.join(self.config.val_labels,file_txt))

            imgs.remove(file_jpg)
            labels.remove(file_txt)


        for i in range(test_count):
            file_jpg = choice(imgs)
            file_txt= file_jpg[:-4]+".txt"

            shutil.copy(os.path.join(self.config.source_dir,file_jpg), os.path.join(self.config.test_images,file_jpg))
            shutil.copy(os.path.join(self.config.source_dir,file_txt), os.path.join(self.config.test_labels,file_txt))

            imgs.remove(file_jpg)
            labels.remove(file_txt)

        

        
