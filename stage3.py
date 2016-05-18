from PIL import Image, ImageDraw
import sys

# Load metro image to modify:
im = Image.open('assets/metro.png')

# Draw box around station:
draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)
del draw

# Save new image:
im.save('assets/metroModified.png', "PNG")
