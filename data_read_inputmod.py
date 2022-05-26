#this file reads in data from a text file and converts it into a 2D array of probabilities


import numpy as np
import matplotlib.pyplot as plt

discreteX9 = np.loadtxt(open("x_datasettest9.csv", "rb"), delimiter=",")
discreteX17 = np.loadtxt(open("x_datasettest17.csv", "rb"), delimiter=",")
discreteX33 = np.loadtxt(open("x_datasettest33.csv", "rb"), delimiter=",")
discreteX65 = np.loadtxt(open("x_datasettest65.csv", "rb"), delimiter=",")
discreteX129 = np.loadtxt(open("x_datasettest129.csv", "rb"), delimiter=",")
discreteX257 = np.loadtxt(open("x_datasettest257.csv", "rb"), delimiter=",")
discreteX513 = np.loadtxt(open("x_datasettest513.csv", "rb"), delimiter=",")

trainingdata9 = np.loadtxt(open("psi_datatrain9.csv", "rb"), delimiter=",")
trainingdata17 = np.loadtxt(open("psi_datatrain17.csv", "rb"), delimiter=",")
trainingdata33 = np.loadtxt(open("psi_datatrain33.csv", "rb"), delimiter=",")
trainingdata65 = np.loadtxt(open("psi_datatrain65.csv", "rb"), delimiter=",")
trainingdata129 = np.loadtxt(open("psi_datatrain129.csv", "rb"), delimiter=",")
trainingdata257 = np.loadtxt(open("psi_datatrain257.csv", "rb"), delimiter=",")
trainingdata513 = np.loadtxt(open("psi_datatrain513.csv", "rb"), delimiter=",")

testingdata9 = np.loadtxt(open("psi_datatest9.csv", "rb"), delimiter=",")
testingdata17 = np.loadtxt(open("psi_datatest17.csv", "rb"), delimiter=",")
testingdata33 = np.loadtxt(open("psi_datatest33.csv", "rb"), delimiter=",")
testingdata65 = np.loadtxt(open("psi_datatest65.csv", "rb"), delimiter=",")
testingdata129 = np.loadtxt(open("psi_datatest129.csv", "rb"), delimiter=",")
testingdata257 = np.loadtxt(open("psi_datatest257.csv", "rb"), delimiter=",")
testingdata513 = np.loadtxt(open("psi_datatest513.csv", "rb"), delimiter=",")

trainLabels9 = np.loadtxt(open("label_datatrain9.csv", "rb"), delimiter=",")
trainLabels17 = np.loadtxt(open("label_datatrain17.csv", "rb"), delimiter=",")
trainLabels33 = np.loadtxt(open("label_datatrain33.csv", "rb"), delimiter=",")
trainLabels65 = np.loadtxt(open("label_datatrain65.csv", "rb"), delimiter=",")
trainLabels129 = np.loadtxt(open("label_datatrain129.csv", "rb"), delimiter=",")
trainLabels257 = np.loadtxt(open("label_datatrain257.csv", "rb"), delimiter=",")
trainLabels513 = np.loadtxt(open("label_datatrain513.csv", "rb"), delimiter=",")

testLabels9 = np.loadtxt(open("label_datatest9.csv", "rb"), delimiter=",")
testLabels17 = np.loadtxt(open("label_datatest17.csv", "rb"), delimiter=",")
testLabels33 = np.loadtxt(open("label_datatest33.csv", "rb"), delimiter=",")
testLabels65 = np.loadtxt(open("label_datatest65.csv", "rb"), delimiter=",")
testLabels129 = np.loadtxt(open("label_datatest129.csv", "rb"), delimiter=",")
testLabels257 = np.loadtxt(open("label_datatest257.csv", "rb"), delimiter=",")
testLabels513 = np.loadtxt(open("label_datatest513.csv", "rb"), delimiter=",")



#accessor functions
def getX():
    discreteX = [discreteX9, discreteX17, discreteX33, discreteX65, discreteX129, discreteX257, discreteX513]
    return discreteX

def getTrain():
    trainingdata = [trainingdata9, trainingdata17, trainingdata33, trainingdata65, trainingdata129, trainingdata257, trainingdata513]
    trainLabels = [trainLabels9, trainLabels17, trainLabels33, trainLabels65, trainLabels129, trainLabels257, trainLabels513]
    print(trainingdata[4].shape)
    return trainingdata, trainLabels

def getTest():
    testingdata = [testingdata9, testingdata17, testingdata33, testingdata65, testingdata129, testingdata257, testingdata513]
    testLabels = [testLabels9, testLabels17, testLabels33, testLabels65, testLabels129, testLabels257, testLabels513]
    return testingdata, testLabels

def getInfo():
    return len(discreteX)

def plot_data(index, data, lambdas, x):
    prob_vals = data[index]
    lambda_val = lambdas[index]

    plt.title("Distribution Plot: " + str(lambda_val))
    plt.plot(x, prob_vals)
    plt.xlabel("X Value")
    plt.ylabel("Probability")
    plt.show()
getTrain()

#i = 0
#while(i<=20):
#    plot_data(i, training_data513, lambdas513, discreteX513)
#    i+= 1

#pass in the training data as the training with the lambda values as what you're trying to learn
