import numpy as np
from keras.utils import load_img, to_categorical
import pandas as pd
import os

def load_image(image_path):
    image = load_img(image_path, target_size=(224, 224))
    image_arr = np.asarray(image)
    return image_arr

def load_from_csv(image_path):
    image = np.genfromtxt(image_path, delimiter=',')
    return image

def load_data_mp(file, target_size=(224, 224)):
  csv_file = 'y_train.csv'
  csv_file = pd.read_csv(csv_file)
  full_image_path = os.path.join('./Color/', file)
  image = load_img(full_image_path, target_size=target_size)
  image = np.asarray(image)
  fns = os.path.splitext(file)[0]
  label = to_categorical(csv_file.iloc[int(fns.split("_")[-1])].target - 1, 
                         len(csv_file['target'].unique())
                         )
  return image, label