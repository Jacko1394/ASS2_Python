#!/usr/bin/python

# this is suitable for a GET - it has no parameters
def initialPage():
	data = "<html><head><title>Demonstration of a webserver</title></head><body>\n"
	data += '<form action="http://127.0.0.1:34567/" method="POST">\n'
	data += '<label for="name">Name:</label>\n'
	data += '<input type="text" name="name" value="" size="" />\n'
	data += '<label for="stationName">Station Namessss:</label>\n'
	data += '<input type="text" name="stationName" value="" size="" />\n'
	data += '<input type="submit" value="Submit">\n'

	data += '</form>'
	data += '</body></html>'
	
	return data

# this is suitable for a POST - it has a single parameter which is 
# a dictionary of values from the web page form.
def respondToSubmit(formData):
	fieldNames = formData.keys()
	
	data = ""
	for field in fieldNames:
		data += "field is " + field + ", value is " + formData[field] + '<br>'
	
	return data