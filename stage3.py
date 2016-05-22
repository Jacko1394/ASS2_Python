#!/usr/bin/env python
import sys
import re
from PIL import Image, ImageDraw


def get_station_pixel_points(station):
	try:
		pixels = open("StationPixelLocation.txt", "r")
	except IOError as e:
		print("ERROR: 'StationPixelLocation.txt' file not found.")
		del e
		sys.exit()

	points = []

	for l in pixels:
		if not l:  # skip blank lines
			continue
		l = l.lower()  # convert to lowercase
		l = re.findall('"([^"]*)"', l)  # extract/separate info

		if not l:  # skip any blank lines (line 1)
			continue

		# If station number found:
		if l[0] == station:
			for i in range(1, 5):
				# Save array of pixel points for text line:
				points.append(int(l[i]))
			break

	pixels.close()
	return points


def draw_pic(station):
	# Load metro image to modify:
	im = Image.open('assets/metro.png')

	# Read pixel point coordinates from text file for drawing:
	p = get_station_pixel_points(station)

	# Draw box around station:
	dr = ImageDraw.Draw(im)
	dr.rectangle(((p[0], p[1]), (p[2], p[3])), outline="red")
	del dr
	im.save('assets/metroModified.png', "PNG")
