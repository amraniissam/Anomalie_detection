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
I plotted the first three recordings as you see below the activity is typically from 0 to 140 observations, the activity is basically up and down and that's how the normal pattern look like. At the beginning there is a drop because it is the beginning of the ECG measurement otherwise it is more towards the normal cyclic circle.
  <div><img src="/img/normal_variation.png" class="displayed"></div>
</p>
<p>  
<h4> Anomaly Data </h4>
In contrary if we take the anomaly data, we see basically now the anomaly data it starts off to be normal but sudden there's a certain drop towards the last observation and we can really see like that is a separation between the normal and anomaly activity.
<img src="/img/Anomaly_variation.png" align="center">
  
</p> 


<h3> Model Training </h3>
  
<p>  
After dividing the data into two parts: training data and test data, I divided each part of the data into two categories: <b> normal </b> and <b> anomaly </b> data.
  
</p> 

  
 

