from time import sleep

import glasscnn
import voronoi_reader,Turnglasslayerstostrucutreandsave
import glm
from glm import length
from PIL import Image, ImageTk
import pickle
import time
import itertools
import tkinter as tk
from tkinter import filedialog

def clamp(a,b,x):
    return max(min(x,b),a)
print("imported libs")

global pixel_data , voronoispace , pixelresult
facingdirection="up"
pixel_data = None
filepath = None



def decode_p(pfinal, num_layers, numcolors):
    intfrombytes = int.from_bytes(pfinal, byteorder='big')
    return [(intfrombytes >> (12 - i * num_layers)) & ((1 << num_layers) - 1) for i in reversed(range(4))]



def decodevoronoi():
    print("reading voronoi")
    voronoispace = voronoi_reader.readvoronoifromzipfile(16,4)
    pixelresult2 = [[decode_p(voronoispace[int(clamp(1,254,pixel.x))][int(clamp(1,254,pixel.y))][int(clamp(1,254,pixel.z))],4,16)
        for pixel in row]for row in pixel_data]

    return pixelresult2

def setfacingto(dir: str,DisplayDirection):
    global facingdirection
    facingdirection = dir
    DisplayDirection.config(text="facing: "+dir)

def generatestructure(dir):
    #pixelresult = [[[1, 2, 3, 4]  for _ in range(4)] for _ in range(4)]
    glassstructure_togenreate=decodevoronoi()
    #print(glassstructure_togenreate)

    Turnglasslayerstostrucutreandsave.export(dir,glassstructure_togenreate,window)


def resize_image_for_tkinter(filepath, max_width, max_height):
    imag = Image.open(filepath)
    orig_width, orig_height = imag.size
    scale = min(max_width / orig_width, max_height / orig_height)
    new_size = (int(orig_width * scale), int(orig_height * scale))

    resized_img = imag.resize(new_size, Image.NEAREST)
    photo = ImageTk.PhotoImage(resized_img)

    return photo


def optionmenuforstructureparameters():
    buttonloadimage.place(relx=-1)

    DisplayDirection = tk.Label(window,text="facing: "+facingdirection , font=("Arial", 24))
    DisplayDirection.place(relx=0.1, rely=0.3, anchor='center')

    Button_face_up = tk.Button(window,text="face up",command=lambda: setfacingto("up",DisplayDirection) , font=("Arial", 16))
    Button_face_up.place(relx=0.1, rely=0.5, anchor='center')
    Button_face_front = tk.Button(window, text="face front", command=lambda: setfacingto("front", DisplayDirection) , font=("Arial", 16))
    Button_face_front.place(relx=0.1, rely=0.6, anchor='center')
    Button_face_down = tk.Button(window, text="face down", command=lambda: setfacingto("down", DisplayDirection) , font=("Arial", 16))
    Button_face_down.place(relx=0.1, rely=0.7, anchor='center')


    EXPORT = tk.Button(window, text="EXPORT", command=lambda: generatestructure(facingdirection) , font=("Arial", 16))
    EXPORT.place(relx=0.1, rely=0.8, anchor='center')
    global filepath
    global photo
    photo = resize_image_for_tkinter(filepath, 640, 500)
    label = tk.Label(window, image=photo)
    label.image = photo  # keep a reference!
    label.place(relx=0.5, rely=0.6, anchor='center')


def elementcolor(colorinput: glm.vec3):
    r = int(colorinput.x)
    g = int(colorinput.y)
    b = int(colorinput.z)
    return f'#{r:02x}{g:02x}{b:02x}'


def waittilimageischosen():
    if pixel_data == None:
        window.after(500, waittilimageischosen)
    else:
        print("chose image")
        optionmenuforstructureparameters()

def openimagebrowser():
    global filepath
    filepath = filedialog.askopenfilename(
        title="Open Image",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff")]
    )
    if filepath:
        # Open image and convert to RGB mode
        img = Image.open(filepath).convert("RGB")
        width, height = img.size
        pixels = img.load()

        # Create 2D list of glm.vec3
        global pixel_data
        pixel_data = [
            [glm.vec3(*pixels[x, y]) for x in range(width)]
            for y in range(height)
        ]




# GUI setup
window = tk.Tk()
window.state('zoomed')
window.title("mcOpticalGenisis")

# Label for displaying the image — this is what was missing
image_label = tk.Label(window,text="mcOpticalGenisis",font=("Arial", 32))
image_label.place(relx=0.5, rely=0.25, anchor='center')

# Button to load image
buttonloadimage = tk.Button(window, text="load image", command=openimagebrowser , font=("Arial", 16))
buttonloadimage.place(relx=0.5, rely=0.5, anchor='center')

window.after(10,func=waittilimageischosen)
window.mainloop()

