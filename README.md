# lin-reg-script
For data science homework 13
Instructions: 
You have been working with Jupyter notebooks this whole time. In this problem, you should not be submitting a jupyter notebook but a script. The script will be a Python file that ends in a .py extension that can be run directly with the “python” command like this:
$ python data_analysis_script.py
This example can be taken as a model Datascript Project Example. You can write the code either with the ccnyhub.org or even better as a back up you can use github codespaces. You click on the “Blank” project and then make that file a .py file.
Either way there is a csv file attached to this problem. You need to download that from Blackboard and upload it to either ccnyhub.org or codespaces. This is the data you will be reading from your script. The imports for your script will be at the top and will look like this:
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
The high level goal will be you will load the data. You will fix up the data by dropping the not a numbers and then you will do the train-test split in preparation for linear regression. You will scatter plot displacement (x-axis) vs acceleration (y-axis) of the training data and save that as a png. Then you will fit the linear regression model and plot the line fit against the testing data to see how well the model does and save that image out as a png. Next you will write the info and summary statistics of the data frame, in addition to the r^2 measure of the fit to a report.txt file. Your code will be called auto-analysis.py
Here are the details
Make a python file called auto-analysis.py (this is not jupyter notebook)
Make sure you have the above imports at the top of your file.
All of the code that is going to be doing the work will be inside of a “main()” function you write, which gets called at the bottom using the “if name == ‘main’” construction as in the Datascript Project Example
Make sure the file auto-mpg.csv is uploaded in the same folder as the auto-analysis.py
Load the auto-mpg.csv data from the file using the pandas “read_csv” code.
Extract the data from the “displacement” column as a numpy array and call it “y” (make sure it has shape (398,1))
Extract the data from the “acceleration” column as a numpy array and call it “X” (make sure it has shape (398,1))
Use train test split to split the X and y into training and test sets
Use matplotlib “subplots” to make a figure and axes object
Use the axis object to scatter plot the training x vs the training y data.
Make sure you use ax to set (label) the x-axis and y-axis “acceleration” and “displacement” respectively.
Use the “fig” object and call “savefig” to save your figure as “xtrain_accel_vs_ytrain_disp.png”
Create a LinearRegression objects and “fit” it with the training x and y.
Find the min and max of the test data and give them names “minX” and “maxX” respectively. You are going to predict their values using your linear model like this:
[miny, maxy] = lr.predict(np.array([minX,maxX]).reshape(-1,1))
Now that you have the end points of your regression line you are going to make a new figure using subplots.
Use the ax to create a new subplot with the testing data
use ax with the “plot” command to plot the X points [minX, maxX] vs [miny, maxy]
As before make sure the x and y axis are labeled
Again save the figure this time as “linear_regression.png”
In a “with open” block, just like in Datascript Project Example create a report just like in the example showing the info, the summary statistics (discribe) but in addition include the R-squared score from lr.score of the test data, and label it as such with a string. This should all be in the report.txt but it should be created fully from your script. This should not be something you edit by hand.
Look up “engine” displacement and “acceleration” Write notes explaining why they seem to be realated as they are. More the “R-squared” score should be 1 if there is a perfect match between the regression prediction and the data, and 0 if the match is poor. Explain why you think the the R2 was high, low or in the middle based on what you see in the scatter plots. Put this in text file called “scriptnotes.txt”
If you are in codespaces you can press the play button to run your script. If you are in ccnyhub.org open a terminal and type
$ python data_analysis_script.py
and if there is an error you are going to need to fix it. 23. You will be turning in five files a) a python file called ‘data_analysis_script.py’ b) a notes file “scriptnotes.txt” c) “xtrain_accel_vs_ytrain_disp.png” d) “linear_regression.png” e) “report.txt”
Note 1: Do not turn in a jupyter notebook. The main point of this exersize is for you to figure out how to run a script not a notebook.
Note 2: You can work out your code first in a jupyter notebook to make sure it runs correctly. Test it. An then convert it to a python file.
