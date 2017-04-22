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

Some Projects Also demands installation of CUDA Toolkit from Nvidia.

To Use it, Make sure to Check out https://developer.nvidia.com/how-to-cuda-python.

Dont forget to download CUDNN for Best Deep Learning Capabilities from https://developer.nvidia.com/cudnn.

## GPU - Accelerated Deep Neural Networks

Start by Downloading Conda https://www.continuum.io/downloads.

Then, Make sure to Create a new Environment. Lets Call it "tensorflow".

```
conda create --name tensorflow python=3.5
```
Now, Just Use: ```activate tensorflow``` from CMD & You're all set.

Use ```pip install tensorflow-gpu```. It usually uses numpy & scipy, So if You can't install it correctly, Use: 
```
conda install scipy
```
