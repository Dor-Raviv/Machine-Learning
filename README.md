# Machine-Learning
This repository is my first public repositories I want to share. 

I will try to upload one project a week. Many of the projects are based on Interests I have & wish to share with everyone.

I will also try to explain & elaborate on my work here for educational purposes.

# Data Visualisation
using t-SNE & sklearn to visualize into 2 dimensions a data set with 70 features. The data set is a monitored body during an exercise.
t-SNE is an algirithm based on Laurens van der Maaten work. (https://lvdmaaten.github.io/software/)

It is a nonlinear dimensionality reduction technique that is particularly well-suited for embedding high-dimensional data into a space of two or three dimensions, which can then be visualized in a scatter plot. Specifically, it models each high-dimensional object by a two- or three-dimensional point in such a way that similar objects are modeled by nearby points and dissimilar objects are modeled by distant points.
The t-SNE algorithm comprises two main stages. First, t-SNE constructs a probability distribution over pairs of high-dimensional objects in such a way that similar objects have a high probability of being picked, whilst dissimilar points have an extremely small probability of being picked. Second, t-SNE defines a similar probability distribution over the points in the low-dimensional map, and it minimizes the Kullback–Leibler divergence between the two distributions with respect to the locations of the points in the map. Note that whilst the original algorithm uses the Euclidean distance between objects as the base of its similarity metric, this should be changed as appropriate.
