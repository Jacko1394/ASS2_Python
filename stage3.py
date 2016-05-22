import sys
import re
from PIL import Image, ImageDraw


def get_station_pixel_points():
	try:
		pixels = open("StationPixelLocation.txt", "r")
	except IOError as e:
		print("ERROR: 'stops.txt' file not found.")
		sys.exit()

	points = ()

	for l in pixels:
		if not l:
			continue
		l = l.lower()  # convert to lowercase
		l = re.findall('"([^"]*)"', l)  # extract/separate info
		print(l)
		l[1] = re.sub('\(.*?\)', '', l[1])  # remove text in brackets



def draw_pic():
	# Load metro image to modify:
	get_station_pixel_points()
	im = Image.open('assets/metro.png')
	dr = ImageDraw.Draw(im)
	dr.rectangle(((100, 100), (200, 300)), fill="blue", outline="red")
	del dr
	im.save('assets/metroModified.png', "PNG")
