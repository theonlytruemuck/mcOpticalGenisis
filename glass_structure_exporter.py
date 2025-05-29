import amulet_nbt as nbt
from amulet_nbt import (
    ByteTag,
    ShortTag,
    IntTag,
    LongTag,
    FloatTag,
    DoubleTag,
    StringTag,
    ListTag,
    CompoundTag,
    ByteArrayTag,
    IntArrayTag,
    LongArrayTag,
    NamedTag,
    utf8_decoder,
    utf8_encoder,
    utf8_escape_decoder,
    utf8_escape_encoder,
)
from mutf8 import decode_modified_utf8, encode_modified_utf8
import tkinter as tk
from tkinter import filedialog


def glasstag(glassname):
    return(
        nbt.CompoundTag({
            'name': nbt.StringTag("minecraft:"+glassname+"_stained_glass"),
            'states': nbt.CompoundTag({}),
            'version': nbt.IntTag(18168865)
        }))

def flatten(array):
    result = []
    for item in array:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def arrayto_inttagarray(array):
    array = flatten(array)
    return [nbt.IntTag(val) for val in array]


def makesublists(dimensions, array):
    l = []
    temporarysublist = []
    for i in range(len(array)):
        if len(temporarysublist) < (dimensions[1] * dimensions[2]):
            temporarysublist.append(array[i])
        else:
            l.append(temporarysublist)
            temporarysublist = [array[i]]
    if temporarysublist:
        l.append(temporarysublist)
    return l

def getoutputpath():
    filepath = filedialog.asksaveasfilename(
    title="Save As",
    defaultextension=".mcstructure",  # optional default extension
    filetypes=[("Minecraft Bedrock Structure Files", "*.mcstructure")])
    if filepath:
        return filepath



def GenerateAndSaveFile(outputpath: str,voxelid: list,dimenssions: list,Window):
    File = nbt.NamedTag(
        nbt.CompoundTag({
            'format_version': nbt.IntTag(1),
            'size': nbt.ListTag([
                nbt.IntTag(dimenssions[0]),
                nbt.IntTag(dimenssions[1]),
                nbt.IntTag(dimenssions[2])
            ]),
            'structure': nbt.CompoundTag({
                'block_indices': nbt.ListTag([
                    #nbt.ListTag(arrayto_inttagarray(makesublists(dimenssions,[voxelid]))),
                    nbt.ListTag(arrayto_inttagarray(voxelid)),
                    nbt.ListTag([IntTag(-1) for _ in range(len(arrayto_inttagarray(voxelid)))])
                ]),
                'entities': nbt.ListTag([]),  # Added entities for completeness
                'palette': nbt.CompoundTag({
                    'default': nbt.CompoundTag({
                        'block_palette': nbt.ListTag([
                            nbt.CompoundTag({
                                'name': nbt.StringTag("minecraft:air"),
                                'states': nbt.CompoundTag({}),
                                'version': nbt.IntTag(18168865)
                            }),
                            glasstag("black"),
                            glasstag("blue"),
                            glasstag("brown"),
                            glasstag("cyan"),
                            glasstag("gray"),
                            glasstag("green"),
                            glasstag("light_blue"),
                            glasstag("lime"),
                            glasstag("magenta"),
                            glasstag("orange"),
                            glasstag("pink"),
                            glasstag("purple"),
                            glasstag("red"),
                            glasstag("light_gray"),
                            glasstag("white"),
                            glasstag("yellow")
                        ]),
                        'block_position_data': CompoundTag({})
                    })
                }),
            }),
            'structure_world_origin': nbt.ListTag([
                nbt.IntTag(0),
                nbt.IntTag(0),
                nbt.IntTag(0)
            ])
        }),
        name="" # The root tag often has an empty name
    )

    #print(mcstructdebug.format_nbt_tree(str(File)))
    outputpath=getoutputpath
    File.save_to(
       outputpath(),
       compressed=False,  # These inputs must be specified as keyword inputs like this.
       little_endian=True,  # If you do not define them they will default to these values
       string_encoder=utf8_escape_encoder
    )
    print("saved")
    Window.destroy()



