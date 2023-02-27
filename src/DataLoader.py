
import pandas as pd
import os 
import numpy as np
from PIL import Image
import cv2

class CalciumData:
    def __init__(self, path) -> None:
        self.data = None
        self.path = path
        self.image_holder = []
        self.load_data_to_data()
        
    def load_data_to_data(self):
        """_summary_: Should load the Calcium Imaging data as a table

        Raises:
            ImportError: No data were detected
        """
        data_dir = sorted(os.listdir(self.path))
        data_formats = ["tiff", "png", "jpeg", "jpg"]
        if not data_dir:
            raise ImportError("The imported Path is wrong and does not hold any data")
        data_list = [i for i in data_dir if "tiff" in i]
        for i in data_list:
            try:
                img = Image.open(self.path +"/" + str(i))
                trial = cv2.imread(self.path +"/" + str(i), 0)
                print(trial.shape)
                imgArray = np.array(img)
                self.image_holder.append(trial)
            except Exception as e:
                print(e)
        
    def __str__(self) -> str:
        """_summary_: The string representation of the class

        Returns:
            str: The name of the class
        """
        return "Data Loader"
    
    def __iter__(self):
        """Construction of the Class as iterator

        Returns:
            _type_: _description_
        """
        self.iterator = 0
        return self
    
    def __next__(self):
        """_summary_

        Raises:
            StopIteration: Whenever no image is left in the holded stack self.image_holder

        Returns:
            _type_: a single image
        """
        if self.iterator > len(self.image_holder):
            raise StopIteration
        images = self.image_holder[self.iterator]
        self.iterator+=1
        return images