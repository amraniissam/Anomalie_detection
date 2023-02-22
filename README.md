# Anomalie_detection

## Description  
<p>
In this project we'll building an anomaly detector using auto-encoder using tensorflow, in order to detect the irregular cardiac activities.
</p>

<h3> Import packages </h3>
<p>
I will import the typical packages: pandas for reading the dataset, matplotlib for visualizing the dataset, tensorflow for building the model especially keras api to build the model, numpy for manipulating the output of the model and then the scikit-learn functions for model selection and for scaling the data.
</p>

<h3> Data </h3>
<p>
  
An electrocardiogram (ECG) is a test that studies how the heart works by measuring its electrical activity. With each heartbeat, an electrical impulse (or "wave") passes through the heart. This wave causes the heart muscle to contract and expel blood from the heart. 

An ECG measures and records the electrical activity that passes through the heart. A doctor can determine if the electrical activity is normal or irregular.
  
This dataset (<a href="https://www.timeseriesclassification.com/Downloads/ECG5000.zip">ECG5000</a> ) contains information on normal and irregular cardiac activity. It contains 5000 observations containing both
normal heart activity and irregular activity.
 
Each row (activity) contains 141 columns. 140 columns are used to measure cardiac activity and one column is the target (first column on the right), class number 1 refers to normal activity, classes number two, three, four and five correspond to irregular cardiac activity.
  
</p> 

<h3> Data Visualisation  </h3>
  
<p>  
<h4> Normal Data </h4>
I plotted the first three recordings as we see below the activity is typically from 0 to 140 observations, the activity is basically up and down and that's how the normal pattern look like. At the beginning there is a drop because it is the beginning of the ECG measurement otherwise it is more towards the normal cyclic circle.
  <div align="center">
     <img src="/img/normal_variation.png">
  </div>
</p>
<p>  
<h4> Anomaly Data </h4>
In contrary if we take the anomaly data, we see basically now the anomaly data it starts off to be normal but sudden there's a certain drop towards the last observation and we can really see like that is a separation between the normal and anomaly activity.
  <div align="center">
     <img src="/img/Anomaly_variation.png">
  </div>
</p> 


<h3> Model Training </h3>
  
<p>  
After dividing the data into two parts: training data and test data, I divided each part of the data into two categories: <b> normal </b> and <b> anomaly </b> data.
  
Our model is an auto-encoder consists of basically on an encoding part and a decoding part. The encoding part does it down sampling it first has 64 units 32 units 16 to 16 units and it finally has an 8 units intermediate layer, this intermediate layer is also called an bottleneck layer, it takes a data in a higher dimension and converts the data into a lower dimension similar to a data compression, what typically a data compression does it learns the embedding of the data into an eight unit vector right in this case, and then to reconstruct back the data again it uses an up sampler which is nothing but the inverse of the down sampler, so it takes 16 30 to 64 and finally the input for us is 140 units the output also will be 140 units 

  
So what we're going to do here is train our model on the normal data and then we'll use the anomalies during the inference process to see how normal they are, so we take a normal data and train our model what is going to happen, the model going to kind of try to reconstruct the normal data because that is our objective to learn the normal data in a proper way but when an irregular data (anomaly data) comes in, it will not be able to reconstruct at all it will be completely the reconstruction error which means the difference between the input and the output, for the anomaly data will be very high compared to the normal data. The term reconstruction error is what we will use to determine if it is an anomaly or normal data.
</p> 
  
<h3> Results </h3> 
<p> 
First I plot the normal data (the actual data) and the auto-encoder output (the reconstructed data), the output data will be similar to the normal data but it will not be exactly same that may be some error, as we see below.
The normal data with red color and the output data (reconstructed data) on blue color, and if we see there are some issues, this is called the reconstruction error, it's the difference between the peaks for blue graph and the red graph. 
For normal data fitting is very well because our model was trained on normal data.
    <div align="center">
     <img src="/img/normal_prediction.png">
  </div>
</p>
<p>   
  
But let's see what happens if we pass to our model an anomaly data. As we see below the anomaly test data on red color and the blue color refers to the auto-encoder output, if we see basically here the error is pretty high (the reconstruction error in this case is pretty high), because in this case our model is not able to reconstruct the input over here.
  <div align="center">
     <img src="/img/anomaly_prediction.png">
  </div>
 </p> 
  
<h3> Futur Detections </h3> 
<p> 
If we wanna classify the future activities in a normal behavior or an anomaly, I will define a loss threshold for our model, for that I was taking the normal test data and calling the model to predict an output for this data, then calculate the error between the inputs and outputs. I did the same thing for the anomaly test data, then I plot a histogramme for the different losses and I choose a threshold = avg(loss(normal Data) + 2*std (loss(normal Data)). 
   <div align="center">
     <img src="/img/threshold.png">
  </div>

For futur activity 
  if (the difference between the input and the output of the model > threshold)  Then the actibity will clasified as an anomaly.
  else (the difference between the input and the output of the model < threshold) Then the actibity will clasified as an normal activity. 
  
</p> 

<p>
    <div align="center">
     <footer>&copy; Copyright 2023 </footer>
  </div>
</p> 
 

