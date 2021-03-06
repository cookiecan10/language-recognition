import json
import os
import re

# Specify all of the languages
languages = ("Dutch", "English")

# variables that can use
datasetDir = "datasets"
modelDir = "models"


# Check if the directory has been created yet, if not, will create it
def makeDir(*args):
    path = ""
    for arg in args:
        path = os.path.join(path,arg)
    if not os.path.isdir(path):
        os.mkdir(path)


# Check if every language has its own directory and sub-directories
def createDirs(languages=languages, datasets=datasetDir, models=modelDir):
    for language in languages:
        makeDir(language)
        makeDir(language, datasets)
        makeDir(language, models)


# Function that checks if a textfile has a corresponding model file
def hasModel(language, filename, models=modelDir):
    fprefix = os.path.splitext(filename)[0]
    if os.path.isfile( os.path.join(language, models, fprefix + ".json")):
        return True
    return False


# A function that takes a text and returns a dictionary of n_grams
def n_gram(text, gramLength):
    d = dict()
    for i in range(len(text)-(gramLength-1)):
        gram = ""
        for j in range(gramLength):
            gram += text[i+j]

        if not gram in d:
            d[gram] = 1
        else:
            d[gram] += 1
    return d

# A function that can count up the total number of n-grams in a model
def gramCounter(model):
    totalGrams = 0
    for key, value in model.items():
        totalGrams += value
    return totalGrams


# Function that takes a text file and stores it into a string
def readText(filename):
    text = ""
    with open(os.path.join(filename), 'r') as fp:
        for line in fp.readlines():
            text += line.strip("\n")
    return text


# TODO a Function that prepares a text by getting rid of things like \n and extra spaces


# Save a model to a file
def saveModel(model, filename):
    with open(filename, 'w') as fp:
        json.dump(model, fp)

# Load a model from a file
def loadModel(filename):
    with open(filename, 'r') as fp:
        return json.load(fp)

# TODO Go through every language directory, and create a model for every .txt file if it hasn't been created yet

# TODO A function that combines 2 models

def combineModels(m1, m2):

    for gram, count in m1.items():

        if gram in m2:
            m2[gram] += count
        else:
            m2[gram] = count
    return m2

# TODO Make a function that adds together all of the models for a single language

# TODO Take an input and calculate the chance for being a specific language

if __name__ == "__main__":

    createDirs() # Create all the directories if they don't exist yet
    ultimateModels = []
    for language in languages:

        for filename in os.listdir(os.path.join(language, datasetDir)):

            fprefix = os.path.splitext(filename)[0]
            m = hasModel(language, filename)
            print("{}: {}, {}".format(language, filename, m))

            if not m:

                text = readText(os.path.join(language, datasetDir, filename))
                model = n_gram(text, 2)
                saveModel(model, os.path.join(language, modelDir, fprefix + ".json"))
                print(gramCounter(model))

        models = []
        p = os.path.join(language, modelDir)
        print(p)
        for m in os.listdir(p):
            print(m)
            models.append(loadModel(os.path.join(language, modelDir, m)))

        ultimateModel = dict()
        for m in models:
            ultimateModel = combineModels(ultimateModel,m)
        print("Ultimate Model ({}): ".format(language))
        print(ultimateModel)
        ultimateModels.append(ultimateModel)

