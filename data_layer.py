import requests, json
from pprint import pprint

from base import DbManager
from models import Club

DB = DbManager()

API_URL = 'http://35.153.66.157/api/{}/{}'

def get_reqest(url):
   response = requests.get(url)
   return json.loads(response.text)

def get_reqests(obj, page):
   response = requests.get(API_URL.format(obj, page) )
   return json.loads(response.text)

def fill_table(model_name, counter, new_model):
   for i in range(1,counter+1):
      url = API_URL.format(model_name, i)
      model = new_model
      model.parse_json(get_reqest(url))
      DB.save(model)
      print('{}. -----------------------'.format(i))
fill_table('club', 10, Club())
