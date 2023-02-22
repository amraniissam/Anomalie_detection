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

  
So what we're going to do here is train our model on the normal data and then we'll use the anomalies during the inference process to see how normal they are.
The term reconstruction error is what we will use to determine if it is an anomaly or normal data.
  
  
  now in the process of taking this data down
sampling it and up sampling it that is some reconstruction error it's a lossy compression so the data
output will not be perfect right now when we take a normal data and train this particular network
what is going to happen is it's going to kind of try to reconstruct the normal data because that is our objective
to learn the normal data in a proper way but when an irregular data that is the anomaly data comes in
it will not be able to reconstruct at all it will be completely the reconstruction error the difference between the input and the
output is called reconstruction error the reconstruction error for the anomaly data
  
  
will be very high compared to the normal data and that's that's the thing we are going to use to determine whether the output is
anomaly or normal right now when we see the graphs and everything we will get a better idea how it looks like
even though it looks more theoretical now once we go into the graph you will be able to visualize it better
now that two ways you this one way of creating a model the other way uh which we are going to
use is is subclassing right the model subclassing uh parameter that is part of tensorflow 2.0
and why we use it is it helps us to use the encoder and decoder separately
easily and the top also i can use it i can go to the layers and use it but this gives me a better way of using the
encoder and decoder suppose i want to use this model only for compressing the data or for
compressing the visualization or take the output compression and run it with this xd boost or random
forest model i can only use the encoder i don't need the decoder at all so this allows me to use the model in
multiple different ways so in this case what i'm doing is i'm creating a class auto encoder right i'm creating an init function this
  
  
  
  
  
  
  
  
  
  
</p> 

  
 

