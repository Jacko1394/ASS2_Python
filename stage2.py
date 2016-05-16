import sys
import re
from stage1 import get_station_list

def generate_station_dropdown():

	stations = get_station_list()

	data = '<select name="station">'

	for station in stations:
		data += '<option value="%s">%s</option>' % (station[0], str(station[1]).title())

	data += '</select>'

	return data


def stage2webpage():
	data = '<html>'
	data += '<head><title>Stage2:s3529497</title></head>'
	data += '<body>'
	data += '<form action="http://127.0.0.1:34567/" method="POST">'

	data += '<label for="station">Station: </label>'
	data += generate_station_dropdown()

	data += '<br><input type="submit" value="Submit">'
	data += '</form></body></html>'

	return data


def respondToSubmit(formData):
	print("received")
	print(formData)

	fieldNames = formData.keys()

	data = ""
	for field in fieldNames:
		print(field)
		data += "field is " + field + ", value is " + formData[field] + '<br>'

	return data


def main():
	print("swag")
	# generate_station_dropdown()
	import webserver
	print("swag")

# ------------------------------- END MAIN ------------------------------- #

if __name__ == "__main__":
	main()
