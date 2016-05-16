#!/usr/bin/env python
import sys
import datetime
import re
from urllib2 import Request, urlopen
import json

MIN_ARGC = 3

if len(sys.argv) < MIN_ARGC:
	print("ERROR: Incorrect number of arguments.")
	sys.exit()
else:
	ARGC = len(sys.argv)  # save number of arguments


def calc_date(date):
	days2add = 0

	# (N) DAYS FROM:
	if str(date[0]).isdigit():
		days2add = int(date[0])  # save (n) number of days
		del date[0:3]  # delete "(n) days from" args

	# DAY SPECIFIER: today/now, tomorrow, next week or weekday:
	date[0] = date[0].lower()  # convert to lowercase
	if date[0] == ("today" or "now"):
		del date
	elif date[0] == "tomorrow":
		days2add += 1
		del date
	elif date[0] == "next":
		days2add += 7
		del date

	# DAYS OF THE WEEK:
	else:
		# Reference tuple of weekdays:
		days = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
		date = str(date[0]).lower()  # convert to lowercase
		# Check weekday match:
		for d in days:
			if date in d:  # mon found in monday
				now = int(datetime.datetime.today().strftime("%w"))
				seeking = days.index(d)
				difference = abs(now - seeking)

				if seeking > now:
					days2add += difference
				else:
					days2add += (7 - difference)
				break

	new_date = datetime.datetime.today() + datetime.timedelta(days=int(days2add))
	return new_date.strftime("%x")


def get_station_location(station):
	try:
		stops = open("stops.txt", "r")
	except IOError as e:
		print("ERROR: 'stops.txt' file not found.")
		sys.exit()

	found = False

	location = ()

	for l in stops:
		l = l.lower()  # convert to lowercase
		l = re.findall('"([^"]*)"', l)  # extract/separate info

		if not l:  # skip blank line (line 1)
			continue

		l[1] = re.sub('\(.*?\)', '', l[1])  # remove text in brackets

		if station in l[1]:
			found = True
			location = (l[1], l[2], l[3])  # save name, lat, lon
			break

	stops.close()

	if not found:
		print("ERROR: Station not found.")
		sys.exit()
	else:
		return location


def get_weather_report(location, date):
	# Calculate number of hours from the current time, based on command arguments:
	hoursfromnow = int((date - datetime.datetime.now()).total_seconds() / 3600)
	# Limit to 168 hours (7 days):
	if hoursfromnow > 168:
		hoursfromnow = 168

	# Forcast API call (% lat, lon):
	weatherapi = Request("https://api.forecast.io/forecast/e24dac09f9fd8317208be7bc7504d270/"
		"%s,%s?units=si&extend=hourly&exclude=currently,minutely,daily,alerts,flags"
		% (location[1], location[2]))
	# Extract JSON into data structure:
	weatherdata = json.loads(urlopen(weatherapi).read())["hourly"]["data"][hoursfromnow]

	# Report string generation:
	report = "***********WEATHER REPORT***********\n" \
		"Location: %s\nLatitude: %s\nLongitude: %s\n" \
		"" % (str(location[0]).title(), location[1], location[2])
	report += "Time: %s\n" \
		"" % datetime.datetime.fromtimestamp(weatherdata["time"]).strftime("%A %b %d, %Y, %I:%M%p")
	report += "Summary: %s\n" \
		"" % weatherdata["summary"]
	report += "Temp: %s degrees celcius\n" \
		"" % weatherdata["temperature"]
	report += "Rain probability: %s%%\nRain quantity: %s mm/hour\n" \
		"" % (weatherdata["precipProbability"] * 100, weatherdata["precipIntensity"])
	report += "Wind speed: %s km/h\nWind direction: %s degrees\n" \
		"" % (weatherdata["windSpeed"], weatherdata["windBearing"])
	report += "************************************"
	return report


def main():
	#try:
		# Variables (arguments converted to lowercase):
		location = get_station_location(str(sys.argv[1]).lower())

		# If date specified, calc the number of days from todays date:
		if ARGC > MIN_ARGC:
			date = calc_date(sys.argv[2:ARGC - 1])
		else:
			date = datetime.datetime.today().strftime("%x")

		# Time extracted from last argument (ARGC - 1):
		time = re.sub(":", "", str(sys.argv[ARGC - 1]).lower())
		# Add '0' to start of time string if needed (for formatting):
		if len(re.sub("\D", "", time)) < 4:
			time = "0" + time

		# Generate date and time object based on analysed arguements:
		if time.isdigit():
			date = datetime.datetime.strptime("%s%s" % (date, time), "%x%H%M")
		else:  # if time.isdigit is not true, am/pm formatting dealt with:
			date = datetime.datetime.strptime("%s%s" % (date, time), "%x%I%M%p")

		print(get_weather_report(location, date))

		# import webserver

	#except Exception as e:
		#print("ERROR: %s" % e.message)
		#sys.exit()


# ------------------------------- END MAIN ------------------------------- #

if __name__ == "__main__":
	main()