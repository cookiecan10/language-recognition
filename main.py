import json
import os

data = {"aaa": 1, "aab": 2}

# Specify all of the languages
languages = ("Dutch", "English")


# Check if every language has its own directory and sub-directories

datasets = "datasets"
models = "models"

for language in languages:
    if not os.path.isdir(language):
        os.mkdir("{}".format(language))

    path = os.path.join(language, datasets)
    if not os.path.isdir(path):
        os.mkdir("{}".format(path))

    path = os.path.join(language, models)
    if not os.path.isdir(path):
        os.mkdir("{}".format(path))


# Function that checks if a textfile has a corresponding model file

def hasModel(language, filename, models=models):
    fprefix = os.path.splitext(filename)[0]
    if os.path.isfile( os.path.join(language, models, fprefix + ".json")):
        return True
    return False



for language in languages:
    for filename in os.listdir(os.path.join(language, datasets)):
        m = hasModel(language, filename)
        print("{}, {}".format(filename, m))
        # fprefix = os.path.splitext(filename)[0]
        # path = os.path.join(language, models, fprefix + ".json")
        # if not os.path.isfile(path):
        #     with open((os.path.join(path)), 'w') as fp:
        #         json.dump(data, fp)


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

print(n_gram("ananas", 2))

# TODO Function that takes a text file and stores it into a string (also take out redundant spaces)

# Save a model to a file
def saveModel(model, filename):
    with open(filename, 'w') as fp:
        json.dump(model, fp)

# Load a model from a file
def loadModel(model, filename):
    with open(filename, 'r') as fp:
        return json.load(fp)

# TODO Go through every language directory, and create a model for every .txt file if it hasn't been created yet

# TODO Make a function that adds together all of the models for a single language

# TODO Take an input and calculate the chance for being a specific language

filename = "n-gram.json"

# with open(filename, 'w') as fp:
#     json.dump(data, fp)


with open(filename, 'r') as fp:
    data2 = json.load(fp)

# print(data2)