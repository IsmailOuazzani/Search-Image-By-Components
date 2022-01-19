# The purpose of this file is to find most relevant images to a query
import math
import json
from webbrowser import get

# Binary search Tree to organize images for each search
class BST:
    left = None
    right = None
    def __init__(self,imgName, rms):
        self.imgName = imgName
        self.rms = rms

    def insert(self,imgName, rms):
        if rms < self.rms:
            if self.left == None:
                self.left = BST(imgName, rms)
            else:
                self.left.insert(imgName, rms)
        else:
            if self.right == None:
                self.right = BST(imgName, rms)
            else:
                self.right.insert(imgName, rms)

    def __repr__(self):
        '''The string representation of a node.
        Here, we convert the value of the node to a string and make that
        the representation.
        We can now use
        a = Node('image1.jpg', 1000)
        print(a) # prints image1.jpg
        '''
        return str(self.imgName)


# return difference between image and search query
def difference(components, query):
    # mean squared error
    ms = 0
    queryLength = len(query)

    for item in query:
        if item in components:
            ms += (100 - components[item])**2 / queryLength
        else:
            ms += 100**2 / queryLength
    # root mean squared
    rms = math.sqrt(ms)
    return rms

# get all elements from json database
def getDatabase(databaseFile):
    f = open(databaseFile)
    database = json.load(f)
    f.close()
    return database

# format database element for searching
#  return imgName and components.
def formatElement(element):
    temp = []
    [temp.extend([k,v]) for k,v in element.items()] 
    imgName = temp[0]
    components = temp[1]
    return imgName, components

# insert database in BST
def sortDatabase(database, query):
    # pop first image of database for the root node of the BST
    root = database.pop()
    imgName, components = formatElement(root)
    rms = difference(components, query)

    # Define BST
    SEARCH = BST(imgName, rms)

    # see what happens if empty !! 
    for element in database:
        # get name and detected objects from element
        imgName, components = formatElement(element)
        rms = difference(components, query)

        # insert in BST
        SEARCH.insert(imgName, rms)
    
    return SEARCH

a = sortDatabase(getDatabase('database.json'), ['traffic light', 'person'])
print(a)
print(a.left)
print(a.right)


# find images with lowest rms
def searchDatabase(SEARCH):
    pass