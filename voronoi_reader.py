import pickle
import zipfile
import os

import sys

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)  # Use EXE location
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Use script location

# Construct the relative path to the zip file
zip_path = os.path.join(BASE_DIR, "voronoispaceautomatedsave.zip")


def readvoronoifromzipfile(numcolors: int,num_layers: int):


    with zipfile.ZipFile(zip_path, 'r') as zf:
        data_bytes = zf.read('voronoispace.pkl')
        voronoispace = pickle.loads(data_bytes)
    print("loaded file")


    print("decoded file")
    return voronoispace
