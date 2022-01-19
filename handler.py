# The purpose of this file is to handle requests from nodeJS using objDetection functions
# to keep the JSON database updated (what each image contains)

import json
import sys
from objDetection import filterObjects
from imageai.Detection import ObjectDetection
import os

def makeDetector():
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(os.path.join(os.getcwd(), 'models', 'resnet50_coco_best_v2.1.0.h5'))
    detector.loadModel()
    return detector

# return list of files to analyze from temp text file
def getImages(tempFile):
    f = open(tempFile)
    imageList = f.read().splitlines()
    f.close()
    return imageList
    
imageList = sys.argv
del imageList[0]
# remove python filename from list of image
# Check if monitorFolder passed a command (single file to analyze) or a json doc (multiple files to analyze)
command = imageList.pop(0)

if command == '-c':
    imageComponents = filterObjects(imageList, makeDetector())
    print(json.dumps(imageComponents))
elif command == '-f':
    # File containing images to analyze
    fileName = imageList[0]
    imageList = getImages(fileName)
    # clear temp.txt
    f = open(fileName,"r+")
    f.truncate(0)
    f.close()
    # get image components and send to monitorFolder.js
    imageComponents = filterObjects(imageList, makeDetector())
    print(json.dumps(imageComponents))
    





    