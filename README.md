# Anomalie_detection

## Description  
<p>
In this project we'll building an anomaly detector using auto-encoder using tensorflow
</p>

<h3> Import packages </h3>
<p>
I will import the typical packages: pandas for reading the dataset, matplotlib for visualizing the dataset, tensorflow for building the model especially keras api to build the model, numpy for manipulating the output of the model and then the scikit-learn functions for model selection and for scaling the data.
</p>

<h3> Data </h3>
<p>
  
I used the ECG5000 <a href="https://www.timeseriesclassification.com/Downloads/ECG5000.zip">Dataset</a>
  
An electrocardiogram (ECG) is a test that studies how the heart works by measuring its electrical activity. With each heartbeat, an electrical impulse (or "wave") passes through the heart. This wave causes the heart muscle to contract and expel blood from the heart. 

An ECG measures and records the electrical activity that passes through the heart. A doctor can determine if the electrical activity is normal or irregular.
  
This dataset contains information on normal and irregular cardiac activity. It contains 5000 observations containing both
normal heart activity and irregular activity.
 
Each row (activity) contains 141 columns. 140 columns are used to measure cardiac activity and one column is the target (first column on the right), class number 1 refers to normal activity, classes number two, three, four and five correspond to irregular cardiac activity.
  
  
</p> 
  

  
  

 
<img src="/img/Anomaly_variation.png" >

