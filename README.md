# Searching images by elements it contains

For this project, I chose to build a "search elements in image" feature, which allows the user to search for images containing specific objects (a car, a cup, a laptop, etc).

## How it works

When the app is initialized, images existing  in the repository are analyzed using the resnet50_coco_best_v2.1.0.h5 pre-trained model (which can recognize 80 different kinds of everyday objects) and the objects that they contain are stored in a JSON file. Newly added images are analyzed as well.
When a search is performed, the images that matches the best with the query are returned.

## Installation

Use package manager to install python dependencies:

```bash
pip install tensorflow==2.4.0
pip install keras==2.4.3 numpy==1.19.3 pillow==7.0.0 scipy==1.4.1 h5py==2.10.0 matplotlib==3.3.2 opencv-python keras-resnet==0.2.0
pip install imageai --upgrade
```

Download the [resnet50_coco_best_v2.1.0.h5](https://github.com/OlafenwaMoses/ImageAI/releases/download/essentials-v5/resnet50_coco_best_v2.1.0.h5/) model for image detection and place it in the models folder.

Install [nodeJS](https://nodejs.org/en/download/).

## Use

Add images to the img folder.

To monitor a folder (initialize it and watch for newly added images), open the project directory and use:

```bash	
node monitorFolder.js
```

To perform a search, use:

```bash	
python query.py -n 5 -objects obj
```

Where the integer followed by -n specifies the number of images to be returned by the search. 

The arguments after -objects are the query (there could be more than one).

example:

```bash	
python query.py -n 10 -objects car person laptop boat
```



## Next steps and limitations

In this section, we discuss the project's current limitations and how to address them in the future.

### Backend

- Tensorflow could be set up to use GPU only, which would reduce the time it takes to analyze each image.
- Images can be stored on a non local database system such as mongoDB for accessibility outside of local network.
- Currently, the search is performed with a python command. In order to connect the backend to a frontend, an API with expressJS can be implemented. It could get search requests with the GET method using parameters to indicate search items.
- The resnet50_coco_best_v2.1.0.h5 model classifies each object with specific words, so an image containing 'person' would not be returned if the user searched for 'engine'. A solution to this issue is to use a synonym API such as the one provided by STANDS4 or build our own synonym finder using large text sets (books) and cosine similarity.
- Remove images from the json database when they are removed from the repository.
- Use a faster sorting algorithm such as quicksort when matching images to queries.

### Frontend

- A user-friendly front end website is needed to perform the search. It could be built with popular frameworks such as VueJS, React, Angular, etc.



 
