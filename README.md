# Reverse-Solving-Schrodinger-s-Equation-with-Machine-Learning
This repo contains Mathematica, python, and Jupyter notebook files that generate datasets, process the datasets, and create predictions through a neural network
Mathematica Notebooks: 
(1) Shooting File: This is the main file that computes the training and testing datasets and labels to be used by the neural network. It solves the Schrodinger Equation using random values of alpha and lambda (potential energy equation coefficients that characterize the potential energy of the system) to produce values of psi. It does this for as many pairs of alpha and lambda are needed for the full training and testing set. You can change the number of discreteX values in the dataset to be compiled in the python file. 
(2) SE Checker: This file takes in values of alpha and lambda and computes the error between the value computed by the numerical solver and the true value using the notion that all elements of the equation moved to 1 side should equal 0. It takes the integral over all x values for a specific alpha/lambda pair to get the error for a given potential energy configuration. We can use this file to generate a table of SE error values to generate a histogram of errors and find where the outliers lie in the scale of errors 
(3) Replace Outlier: This is the file that replaces values of psi, alpha, and lambda in a given file with the goal of removing and replacing outliers in the dataset. 
Python Files: 
(1) Data_read_inputmod: This file compiles the datasets exported by Mathematica to prepare to pass into the jupyter notebook. It compiles datsets generated with varying discrete x values with the goal of finding the best neural network structure and create the best input:hidden layer ratio. 
Jupyter Notebook Files:
(1) Probability-Lambda-Alpha-NN-Input-Mod: This is the file that evaluates the datasets in a neural network. It imports the python file above to gain access to the datasets from Mathematica. Based on the second index value in the 2nd cell, you can change the number of discrete X values used in the neural network and consequentally, which Mathematica file to use in the neural network. 

I have also included text files to be modified each time you run the mathematica dataset and export under the same name. 
