import json
import os

data = {"aaa": 1, "aab": 2}

# Specify all of the languages
languages = ("Dutch", "English")

# Check if every language has it's own directory and sub-directories

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

# TODO Make a function that checks if a textfile has a corresponding model file

for language in languages:
    for filename in os.listdir(os.path.join(language, datasets)):
        fprefix = os.path.splitext(filename)[0]
        print(fprefix)
        path = os.path.join(language, models, fprefix + ".json")
        if not os.path.isfile(path):
            with open((os.path.join(path)), 'w') as fp:
                json.dump(data, fp)


# TODO Make a function that takes a textfile and makes a model with it

# TODO Make a function that saves a model to a json file

# TODO Go through every language directory, and create a model for every .txt file if it hasn't been created yet

# TODO Make a function that adds together all of the models for a single language

# TODO Take an input and calculate the chance for being a specific language

filename = "n-gram.json"

# with open(filename, 'w') as fp:
#     json.dump(data, fp)


with open(filename, 'r') as fp:
    data2 = json.load(fp)

# print(data2)