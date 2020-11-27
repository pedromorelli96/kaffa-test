#####################################################
# Kaffa - Pre-qualification Test
# 6) Rest Client - World Clock
# Name: Pedro Rodrigo Ramos Morelli
# E-mail: pedromorelli96@gmail.com
#####################################################

# datetime used to convert time zone
from datetime import datetime, timezone
# requests used to query server and manipulate json
import requests

# Server URL
URL = "http://worldclockapi.com/api/json/utc/now"

# Response from requesting the server URL
response = requests.get(URL)

# Converts json response to a dictionary
rjson = response.json()

# {'$id': '1', 'currentDateTime': '2020-11-27T00:00Z', 'utcOffset': '00:00:00', 'isDayLightSavingsTime': False,
# 'dayOfTheWeek': 'Friday', 'timeZoneName': 'UTC', 'currentFileTime': 132509088217975827, 'ordinalDate': '2020-332', 
# 'serviceResponse': None}

# Gets 'currentDateTime' key from dictionary
date_time_UTC = rjson['currentDateTime']

# Converts date_time_UTC string to datetime object
tm = datetime.strptime(date_time_UTC,r"%Y-%m-%dT%H:%MZ")
print("UTC Date and Time: ")
# Converts datetime object to adequate format
print(tm.strftime('%Y-%m-%d %H:%M'))
print("-"*20)
# Converts the timezone from UTC to local (GMT-3)
tm = tm.replace(tzinfo=timezone.utc).astimezone(tz=None)
print("Local Date and Time (GMT-3):")
print(tm.strftime('%Y-%m-%d %H:%M'))