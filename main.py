#from cgi import test
#from distutils.ccompiler import new_compiler
import src.imgGrab as imgGrab
import src.genPxart as gP
from PIL import Image
import os
import src.vidMaker as vidMaker
import random
import src.titles as titles
import json



# Load config file
with open('config.json', 'r') as c:
    config = json.load(c)

# Settings
if config["Generate Images"].lower() == 'true': # Do you want to generate images?
    genImages = True
else:
    genImages = False
if config["Generate Videos"].lower() == 'true': # Do you want to generate videos?
    genVideos = True 
else:
    genVideos = False
amount = config["Amount"]

# What is this
path = "src\\download"
base = Image.open(r"src/base.png").copy()
prompts = []
baseVids = []

# Base video options
for file in os.listdir("src\\basevids"):
    baseVids.append(f'src\\basevids\\{file}')

# Initialize things
Grabber = imgGrab.grabber(path, amount)
Gen = gP.generator(base, 0.8)
vm = vidMaker.vidMaker()
title = titles.titler()

# Generate images
if genImages:
    # Get Prompts
    with open("prompts.txt", 'r') as pts:
        for line in pts.readlines():
            prompts.append(line.strip())

    # Download prompts
    for prompt in prompts:
        print(f"prompt: {prompt}")
        Grabber.grab(prompt)

        # Add images to backplate
        for file in os.listdir("src\\download"):
            newImg = Gen.generate(Image.open(f"src\\download\\{file}"))
            newImg.save(f"src\\done\\{prompt}-{os.path.splitext(file)[0]}.png")
            imgNumber = len(os.listdir('src\\done'))
            print(f"An image has been generated {imgNumber}")

        # Clean up
        for file in os.listdir("src\\download"):
            os.remove(f"src\\download\\{file}")

# Generate videos
if genVideos:
    vm.makeVidsFI()

    for file in os.listdir("src\\vidpart"):

        vm.combVid(random.choice(baseVids), f"src\\vidpart\\{file}", os.path.splitext(file)[0]) # Combine result with placing video

        os.remove(f"src\\vidpart\\{file}")

        

# Doesn't work and isn't finished
""" 
if uploadVideos:
    for file in os.listdir("src\\output"):
        upl.upload(f"src\\output\\{file}", title.create(file), "public")
"""

# Finished
lst = os.listdir("src\\output")
number_files = len(lst)

print("-------------------------------------------")
print(f"Amount of videos available: {number_files}")
print("-------------------------------------------")
