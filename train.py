import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf 
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import Model
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.losses import mae 


data=pd.read_csv('ECG_ALL_Data.txt', sep='  ', header=None)
x_train, x_test, y_train, y_test = train_test_split(data, data.values[:, 0:1], train_size=0.8, random_state=0)

transformer= MinMaxScaler()
data_transformed= transformer.fit(x_train)

x_train_transformed=transformer.transform(x_train)
x_test_transformed=transformer.transform(x_test)


normal_x_train_transformed=pd.DataFrame(x_train_transformed).add_prefix('f').query('f0==0').values[:, 1:]
anomaly_x_train_transformed=pd.DataFrame(x_train_transformed).add_prefix('f').query('f0 > 0').values[:, 1:]


normal_x_test_transformed=pd.DataFrame(x_test_transformed).add_prefix('f').query('f0==0').values[:, 1:]
anomaly_x_test_transformed=pd.DataFrame(x_test_transformed).add_prefix('f').query('f0 > 0').values[:, 1:]

class AutoEncoder(Model):
  def __init__(self):
    super(AutoEncoder, self).__init__()
    self.encoder = Sequential([
        Dense(64, activation="relu"),
        Dense(32, activation="relu"),
        Dense(16, activation="relu"),
        Dense(8, activation="relu")])
    
    self.decoder=tf.keras.Sequential([
        Dense(16, activation="relu"),
        Dense(32, activation="relu"),
        Dense(64, activation="relu"),
        Dense(140, activation="sigmoid")])
    
  def call(self, x):
    encoded=self.encoder(x)
    decoded=self.decoder(encoded)
    return decoded

model= AutoEncoder()
early_stopping=EarlyStopping(monitor='val_loss',
                             patience=2,
                             mode='min')                      
                                                
model.compile(optimizer='adam', loss='mae')


history= model.fit(normal_x_train_transformed,normal_x_train_transformed,
                   epochs=70,
                   batch_size=128,
                   validation_data=(x_train_transformed[:,1:],x_train_transformed[:,1:]),
                   shuffle=True,
                   callbacks=[early_stopping])


dump(model, 'anomalie_detection_model.joblib')

