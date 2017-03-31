# Machine-Learning

<div align="center">
  <img src="http://images.iop.org/objects/phw/news/15/9/18/neuron.jpg" ><br>
</div>

Using ML for Everyday challanges is Fun. This is just the tip of the Iceberg!

We'll Cover all sorts of ML projects, From Data Science to Predicting the Future.

## Getting Started

Use the instructions on each project. Make sure to get all the pre-requisitins ahead of running. 
I'll try to explain what are the results we see & analyze them.

### Prerequisitions 

Each Project has it's own Python libraries. But all of them require:

```
Python 2.7 / python 3.5
```
And Python Libraries for each project Are listed on top of the ```project.py```.

# Data Visualisation
## Problem: We have so much Data & we can't figure out anything out of it! 
In recent times, We collect so much Data about everything! From our habits & food, To Car sensors. Data is everywhere! What is the connection between Our Workout Habits & Muscle movement? 
The following Script will try to answer that!
### Prerequisitions
Using python's ```sklearn``` library, we will Reduce over 70 Columns of Data, Into only 2 Dimensions! 

## Results

<div align="center">
  <img src="https://s18.postimg.org/yjab7kd7t/t-sne.png"><br><br>
</div>

### The Science behind it...

using t-SNE & sklearn to visualize into 2 dimensions a data set with 70 features. The data set is a monitored body during an exercise.
t-SNE is an algirithm based on Laurens van der Maaten work. (https://lvdmaaten.github.io/software/)

It is a nonlinear dimensionality reduction technique that is particularly well-suited for embedding high-dimensional data into a space of two or three dimensions, which can then be visualized in a scatter plot. Specifically, it models each high-dimensional object by a two- or three-dimensional point in such a way that similar objects are modeled by nearby points and dissimilar objects are modeled by distant points.

