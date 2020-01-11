
# Temperature Showing tool in Python .
# Author : Nilanjan Chakraborty
# Date   : 5th January ,2020
# Time   : 2:58 AM
# Licence: GNU GPL

import urllib
import requests

def getClimate(CityName):
    url="https://www.meteoprog.pl/en/weather/"+str(CityName)+"/"
    weblink=urllib.urlopen(url)
    webdata=weblink.read()
    temp_data=[]
    for i in webdata.split():
        if 'class="temperature_value">' in i:
            temp_data.append(i)
    stops=['@', '_', '!', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', '\\', '|', '}', '{', '~', ':']
    temp=""
    for i in temp_data[0][26:29]:
        for j in stops:
            if i==j:
                temp=temp+temp_data[0][26:29].replace(i,'')
                return temp
    return temp_data[0][26:29]


city=raw_input("Enter City Name: ")
temperature_value=getClimate(city)
degree_sign= u'\N{DEGREE SIGN}'
temperature_value=str(temperature_value)+degree_sign+"C"
show="Temperature in "+city+" = "
print show,temperature_value
