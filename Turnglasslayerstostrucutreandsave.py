import glass_structure_exporter
import numpy as np




def export(facingdirection,glassstructure,Window):
    F2="C:/Users/GMS/Documents/glass/bubble_column2.mcstructure"


    def dimensions(array):
        return [len(array), len(array[0]), len(array[0][0])]

    def swizzle(array: list,dir: str):
        dim=dimensions(array)
        if dir=="up":
            return np.transpose(array,(1,2,0)).reshape(dim[1],dim[2],dim[0])[:,:,::-1].tolist()
        elif dir=="down":
            return np.transpose(array,(1,2,0)).reshape(dim[1],dim[2],dim[0])[:,::-1,:].tolist()
        elif dir=="front":
            return np.rot90(array, k=-1, axes=(0, 1)).tolist()

    dimensionsinp=dimensions(glassstructure)
    #print("glassstructure: ",glassstructure)

    outputglassstructure = [[[0 for _ in range(2*len(glassstructure[0][0]))] for _ in range(len(glassstructure[0]))] for _ in range(len(glassstructure))]
    dimensionsout=dimensions(outputglassstructure)
    #print("outputglassstructure: ",outputglassstructure)

    for x in range(dimensionsinp[0]):
        for y in range(dimensionsinp[1]):
            for layer in range(dimensionsinp[2]):
                outputglassstructure[x][y][layer*2]=glassstructure[x][y][layer]+1

    outputglassstructure = swizzle(outputglassstructure , facingdirection)
    dimensionsout = dimensions(outputglassstructure)



    glass_structure_exporter.GenerateAndSaveFile(F2,outputglassstructure,dimensionsout,Window)