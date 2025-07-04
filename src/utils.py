import os
import numpy as np # type: ignore
import pandas as pd  # type: ignore
import pickle


import sys

from src.exception import CustomException

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        
        os.makedirs(dir_path,exist_ok=True)
        
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_path)
    except Exception as e:
        raise CustomException(e,sys)