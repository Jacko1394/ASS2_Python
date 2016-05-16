import sys
import re
from stage1 import get_station_list


dates = ('Today', 'Tomorrow', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')


def generate_label(text, newline):
	data = '<label>%s</label>' % text
	if newline:
		data += '<br>'
	return data


def generate_station_dropdown():
	stations = get_station_list()
	data = '<select name="station">'

	for station in stations:
		data += '<option value="%s">%s</option>' % (station[0], str(station[1]).title())

	data += '</select>'
	return data


def generate_date_dropdown():
	data = '<select name="date">'

	for i in range(0, len(dates)):
		data += '<option value="%s">%s</option>' % (i, dates[i])

	data += '</select>'
	return data


def generate_time_dropdown():
	data = '<select name="station">'

	data += '</select>'
	return data


def stage2webpage():
	# Initialisation:
	data = '<html>'
	data += '<head><title>Stage2:s3529497</title></head>'
	data += '<body>'
	data += '<form action="http://127.0.0.1:34567/" method="POST">'
	# Add labels:
	data += generate_label('***WEATHER/TRAIN PROGNOSTICATION DIVINER***', True)
	data += generate_label('Station: ', False)
	# Add station dropdown menu:
	data += generate_station_dropdown() + '<br>'

	data += generate_label('Date: ', False)
	data += generate_date_dropdown() + '<br>'

	data += generate_label('Time: ', False)
	data += generate_time_dropdown() + '<br>'

	data += '<input type="submit" value="Submit">'
	data += '</form></body></html>'

	return data


def respond2webpage(formData):
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
