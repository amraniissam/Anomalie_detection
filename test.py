import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf 
from tensorflow.keras.losses import mae 



data=pd.read_csv('ECG_ALL_Data.txt', sep='  ', header=None)
x_train, x_test, y_train, y_test = train_test_split(data, data.values[:, 0:1], train_size=0.8, random_state=0)

transformer= MinMaxScaler()
data_transformed= transformer.fit(x_train)


x_test_transformed=transformer.transform(x_test)


normal_x_test_transformed=pd.DataFrame(x_test_transformed).add_prefix('f').query('f0==0').values[:, 1:]
anomaly_x_test_transformed=pd.DataFrame(x_test_transformed).add_prefix('f').query('f0 > 0').values[:, 1:]




model= load('anomalie_detection_model.joblib')

test_prediction_normal = model.predict(normal_x_test_transformed)
normal_loss = mae(test_prediction_normal, normal_x_test_transformed)


threshold = np.mean(normal_loss)+ 2*np.std(normal_loss)


test_prediction_anomaly = model.predict(anomaly_x_test_transformed)
anomaly_loss = mae(test_prediction_anomaly, anomaly_x_test_transformed)


plt.figure(figsize=(12,6))
plt.hist(normal_loss, bins=50, label="Normal")
plt.hist(anomaly_loss, bins=50, label="Anomaly")
plt.axvline(threshold, color='r',linewidth=3, linestyle='dashed', label='{:0.3f}'.format(threshold))
plt.legend(loc='upper right')
plt.show()