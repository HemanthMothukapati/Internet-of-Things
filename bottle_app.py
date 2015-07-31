# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, template
import get_weather
import requests

@route('/tempmap')
def hello_project():
  req = requests.get('https://data.sparkfun.com/output/aGOE6rY5mxcxX1GNnOKq.json?page=1')
  data = req.json()
  rows=[]
  for i in range(0,20):
    lat = data[i]['latitude']
    lon = data[i]['longitude']
    tempc=data[i]['temperature']
    light=data[i]['light']
    rows.append((lat,lon,tempc,light))
  return template('tempmap', rows=rows)

@route('/templight')
def templight():
  return template('bar')
    
@route('/iot')
def iot():
  return template("iot")
  
application = default_app()  
