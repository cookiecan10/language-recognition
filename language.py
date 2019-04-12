import os
import pickle
"""
Language class, deals with its own stuff instead of having to do everything myself.
"""

class Model:

    def __init__(self, gramLength):
        self.model = dict()
        self.numOfGrams = 0

        self.gramLength = gramLength # the N in n-gram, (bi-gram, tri-gram, etc)

    # Take a single n-gram and puts it into the model
    def addGram(self, gram):

        if not gram in self.model:
            self.model[gram] = 1
        else:
            self.model[gram] += 1

        self.numOfGrams += 1

    # A function that takes a text and puts the n-grams into the model
    def addTextAsGrams(self, text):

        for i in range(len(text) - (self.gramLength - 1)):
            gram = ""
            for j in range(self.gramLength):
                gram += text[i + j]

            self.addGram(gram)

    # For testing purposes, count all of the grams in the model.
    def gramCounter(self):
        totalGrams = 0
        for key, value in self.model.items():
            totalGrams += value
        return totalGrams

    # combines model into this model
    def combineModel(self, m2):
        self.numOfGrams += m2.numOfGrams
        for gram, count in m2.model.items():

            if gram in self.model:
                self.model[gram] += count
            else:
                self.model[gram] = count

    # Returns individual gram chance,  gram_occurrence / total_grams
    # WARNING: Has not been tested yet
    def gramChance(self, gram):
        if gram in self.model:
            return self.model[gram] / self.numOfGrams
        else:
            return .001 / self.numOfGrams

    # Function that takes in some text and calculates the chance that it's the same language as this model
    # WARNING: Has not been tested yet!!!!
    def realChanceCalculationThing(self, text):
        chance = 1
        for i in range(len(text) - (self.gramLength - 1)):
            gram = ""
            for j in range(self.gramLength):
                gram += text[i + j]
            chance *= self.gramChance(gram)
        return chance


class Language:

    def __init__(self, language, subDir=""):

        self.language = language

        self.subDir = os.path.join(subDir,language) # Wil probably add the possibility to specify a subdirectory, to keep main folder empty

        self.datasetDir = "datasets"
        self.modelDir = "n-grams"

        self.bi_grams = [] # probably not needed, will only load 1 bi_gram at a time in order to build ultiBi_gram
        self.tri_grams = []

        self.ultiBi_gram = Model(2)
        self.ultiTri_gram = Model(3)

    # Check if the directory has been created yet, if not, will create it
    def makeDir(self, *args):
        path = ""
        for arg in args:
            path = os.path.join(path, arg)
        if not os.path.isdir(path):
            os.mkdir(path)

    # Check if every language has its own directory and sub-directories
    def createDirs(self):
        self.makeDir(self.subDir)
        self.makeDir(self.subDir, self.datasetDir)
        self.makeDir(self.subDir, self.modelDir)

    # Function that checks if a textfile has a corresponding model file
    def isModel(self, filename):
        fprefix = os.path.splitext(filename)[0]
        if os.path.isfile(os.path.join(self.subDir, self.modelDir, fprefix + ".model")):
            return True
        return False

    # Save a model to a file
    # IMPORTANT: This version uses Pickle, NOT Json!!
    def saveModel(self, model, filename):
        with open(filename, 'wb') as handle:
            pickle.dump(model, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # Load a model from a file
    # IMPORTANT: This version uses Pickle, NOT Json!!
    def loadModel(self, filename):
        with open(filename, 'rb') as handle:
            return pickle.load(handle)

    # Function that takes a text file and stores it into a string
    def readText(self, filename):
        text = ""
        with open(os.path.join(filename), 'r') as fp:
            for line in fp.readlines():
                text += line.strip("\n")
        return text

    # TODO take out all numbers
    # function that prepares a piece of text for grammification
    def prepare(self, text):
        return text.replace("\n","").replace("  ", " ").replace("'","").replace("(","").replace(")","")
    
    # TODO Function that makes and saves a model for every dataset item
    def makeModel(self, filename, length=2):
        
        text = self.readText(filename)
        text = self.prepare(text)
        
        m = Model(length)
        
        m.addTextAsGrams(text)
        return m
    

    # TODO Function: go through every model in the model file, and add it to the ulti-model.
    def makeUltimodels(self):
        for filename in os.listdir(os.path.join(self.language, self.datasetDir)):
            text = self.readText(os.path.join(self.language, self.datasetDir, filename))

            text = self.prepare(text)
            
            self.ultiBi_gram.addTextAsGrams(text)
            self.ultiTri_gram.addTextAsGrams(text)
        
    # TODO Function that checks if an ulti-model already exists or not

    # Saving ultimodels
    def saveUltiModels(self):
        self.saveModel(self.ultiBi_gram, os.path.join(self.language, "bi_gram"))
        self.saveModel(self.ultiTri_gram, os.path.join(self.language, "tri_gram"))

    def loadUltiModels(self):
        self.ultiBi_gram = self.loadModel(os.path.join(self.language,"bi_gram"))
        self.ultiTr_gram = self.loadModel(os.path.join(self.language,"tri_gram"))
    
    # TODO Function that returns a chance (using ulti-models and such)
    def calcBiChance(self, text):
        chance = 1
        chance *= self.ultiBi_gram.realChanceCalculationThing(text)
        return chance

    def calcTriChance(self, text):
        chance = 1
        chance *= self.ultiTri_gram.realChanceCalculationThing(text)
        return chance

