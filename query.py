# The purpose of this file is to find most relevant images to a query
import math
import json
import sys

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

# return list of images with their RMS error
def getRMS(database, query):
    SEARCH = []
    d = database.pop()

    for imgName, components in d.items():
        rms = difference(components, query)
        temp_dic = {'name': imgName, 'rms': rms}
        SEARCH.append(temp_dic)

    return SEARCH

# Returns n images with lowest RMS error values, i.e. that match the best the query
def lowestRMS(SEARCH,n):
    sort = sorted(SEARCH, key= lambda i: i['rms'])

    # only keep image paths
    paths = []
    i = 0
    while len(paths) < n and len(paths) < len(sort):
        paths.append(sort[i]['name'])
        i +=1

    return paths


# Python command
command  = sys.argv
n = int(command[2]) # obtain n
query = command [4:] #obtain query

database = getDatabase('database.json')
sortedDatabase = getRMS(database, query)
print(lowestRMS(sortedDatabase, n))