import re
import datetime
from stage1 import calc_date, get_station_list, get_weather_report
from stage3 import draw_pic
import webserver

ampm = ('AM', 'PM')
pageinfo = ("station", "date", "timehour", "timeampm")
dates = ('Today', 'Tomorrow', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
stations = get_station_list()


def generate_label(text, newline):
	data = '<label>%s</label>' % text
	if newline:
		data += '<br>'
	return data


def generate_station_dropdown():
	data = '<select name=%s>' % pageinfo[0]

	for station in stations:
		data += '<option value="%s">%s</option>' % (station[0], str(station[1]).title())

	data += '</select>'
	return data


def generate_date_dropdown():
	data = '<select name=%s>' % pageinfo[1]

	for i in range(0, len(dates)):
		data += '<option value="%s">%s</option>' % (i, dates[i])

	data += '</select>'
	return data


def generate_time_dropdown():
	# Hours:
	data = '<select name=%s>' % pageinfo[2]
	for i in range(1, 13):
		data += '<option value="%s:00">%s:00</option>' % (i, i)
	data += '</select>'
	# AM/PM:
	data += '<select name=%s>' % pageinfo[3]
	data += '<option value="0">AM</option>'
	data += '<option value="1">PM</option>'
	data += '</select>'

	return data


def stage2webpage():
	# Initialisation:
	data = '<html>'
	data += '<head><title>Stage2 : s3529497</title></head>'
	data += '<body>'
	data += '<form action="http://127.0.0.1:34567/" method="POST">'
	# Add labels:
	data += generate_label('***WEATHER/TRAIN PROGNOSTICATION DIVINER***', True) + '<br>'
	data += generate_label('Station: ', False)
	# Add station dropdown menu:
	data += generate_station_dropdown() + '<br><br>'
	# Add date dropdown menu:
	data += generate_label('Date: ', False)
	data += generate_date_dropdown() + '<br><br>'
	# Add time dropdown menu:
	data += generate_label('Time: ', False)
	data += generate_time_dropdown() + '<br><br>'
	# Add submit button:
	data += '<input type="submit" value="Submit"><br><br>'
	data += generate_label('**************************************************', True)
	data += '</form></body></html>'
	return data


def respond2webpage(formData):
	# Format date arg:
	date = [dates[int(formData[pageinfo[1]])]]
	date = calc_date(date)

	# Format time arg:
	time = re.sub(':', '', formData[pageinfo[2]])
	if len(time) < 4:
		time = '0' + time + ampm[int(formData[pageinfo[3]])]
	else:
		time += ampm[int(formData[pageinfo[3]])]

	# Format date for weather report call:
	date = datetime.datetime.strptime("%s%s" % (date, time), "%x%I%M%p")

	# Format station arg:
	location = ()

	for s in stations:
		if s[0] == str(formData[pageinfo[0]]):
			location = (s[1], s[2], s[3])
			break

	print(formData[pageinfo[0]])

	# Draw box around station name:
	# print('dsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsddsdsdsd')
	draw_pic()

	# Initialisation:
	data = '<html>'
	data += '<head><title>Stage2 : s3529497</title></head>'
	data += '<body>'
	# Format report for HTML:
	data += re.sub("\n", "<br>", get_weather_report(location, date)) + '<br>'
	data += '<img src="metroModified.png" alt="assets/metro.png">'
	data += '</body></html>'

	return data
