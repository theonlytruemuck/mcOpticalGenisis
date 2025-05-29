import glm
from glm import length
import pickle

def mix(val1,val2,x):
    return val1*(1-x)+val2*x

colorindexes = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]#[0,4,13,14]#

allcolors = [
    glm.vec3(26, 26, 26),      # black0
    glm.vec3(50, 76, 177),     # blue1
    glm.vec3(102, 76, 50),     # brown2
    glm.vec3(76, 128, 151),    # cyan3
    glm.vec3(76, 76, 76),      # gray4
    glm.vec3(102, 128, 50),    # green5
    glm.vec3(102, 151, 215),   # light blue6
    glm.vec3(128, 205, 26),    # lime7
    glm.vec3(177, 76, 215),    # magenta8
    glm.vec3(215, 128, 50),    # orange9
    glm.vec3(241, 128, 165),   # pink10
    glm.vec3(128, 62, 177),    # purple11
    glm.vec3(153, 52, 52),     # red12
    glm.vec3(151, 151, 151),   # silver13
    glm.vec3(255, 255, 255),   # white14
    glm.vec3(229, 229, 50)     # yellow15
]
colorsl = [allcolors[val] for val in colorindexes]
numcolors = len(colorsl)
allcolor_names = [
    "black",
    "blue",
    "brown",
    "cyan",
    "gray",
    "green",
    "light blue",
    "lime",
    "magenta",
    "orange",
    "pink",
    "purple",
    "red",
    "silver",
    "white",
    "yellow"
]
color_names = [allcolor_names[val] for val in colorindexes]

