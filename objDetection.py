from xml.etree.ElementPath import find
from imageai.Detection import ObjectDetection
import os

#https://towardsdatascience.com/object-detection-with-10-lines-of-code-d6cb4d86f606

# Returns all objects in an image and percentage probabilities and box_points
def findObjects(image, detector):
    # detect objects in image
    execution_path = os.getcwd()
    imgPath = os.path.join(execution_path ,'img', image )
    detections = detector.detectObjectsFromImage(input_image=imgPath, output_type="array")
    # obtain objects
    objects = detections[1]
    return objects

# Filter image objects to get a list of unique objects in an image and their percent probability
def filterObjects(images, detector):
    # unique objects in all images, does not contain duplicates, only contains highest probability
    components = {}
    # all objects in image, contains duplicates
    for image in images:
        # temp value that holds components of one image
        img = image[4:] #get rid of /img
        temp_value = {}
        mixed_objects = findObjects(img, detector)
        for obj in mixed_objects:
            if obj['name'] not in temp_value:
                temp_value[obj['name']] = obj['percentage_probability']
            else:
                if temp_value[obj['name']] < obj['percentage_probability']:
                    temp_value[obj['name']] = obj['percentage_probability']
        components[img] = temp_value
    return components



