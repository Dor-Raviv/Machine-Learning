from time import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

__Project_Number__ = 1
__Author__ = 'Dor Raviv'
__Date__ = '26/3/2017'

'''
Using Sklearn to process & visualise a data set using t-SNE algorithm...
'''

# Getting Data set from the web.

data_frame = pd.read_csv('https://d396qusza40orc.cloudfront.net/predmachlearn/pml-training.csv', low_memory=False)
num_rows = data_frame.shape[0]

# Cleaning he data
# Count the number of missing elements (NaN) in each column
counter_nan = data_frame.isnull().sum()
counter_without_nan = counter_nan[counter_nan == 0]
# removing the columns with missing elements
data_frame = data_frame[counter_without_nan.keys()]
# Removing the first 7 columns that contain no discriminative info
data_frame = data_frame.ix[:, 7:]
# debugging
# columns = data_frame.columns
# print columns

# Creating feature vectors - Mean of 0 & SD of 1 (Normalizing)
x = data_frame.ix[:, :-1].values
standard_scalar = StandardScaler()
# we have 70 columns - so 70 "features"
x_std = standard_scalar.fit_transform(x)

# get class label data
y = data_frame.ix[:, -1].values
# encode the class label
class_labels = np.unique(y)
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# split the data into training set and test set
test_percentage = 0.1
x_train, x_test, y_train, y_test = train_test_split(x_std, y, test_size=test_percentage, random_state=0)

# Measuring the visualisations process
start_time = time()
# Using t-SNE t-distributed Stochastic Neighbor Embedding for visualization & dimensional reduction

from sklearn.manifold import TSNE

# n_components = How many dimensions we wish to see.
tsne = TSNE(n_components=2, random_state=0)
x_test_2d = tsne.fit_transform(x_test)

print "Finished visualisation of data set. It took {0} seconds.".format(time() - start_time)

# scatter plot the sample points among 5 classes
markers = ('s', 'd', 'o', '^', 'v')
color_map = {0: 'red', 1: 'blue', 2: 'lightgreen', 3: 'purple', 4: 'cyan'}
plt.figure()
for idx, cl in enumerate(np.unique(y_test)):
    plt.scatter(x=x_test_2d[y_test == cl, 0], y=x_test_2d[y_test == cl, 1], c=color_map[idx], marker=markers[idx],
                label=cl)
plt.xlabel('X in t-SNE')
plt.ylabel('Y in t-SNE')
plt.legend(loc='upper left')
plt.title('t-SNE visualization of test data')
plt.show()
