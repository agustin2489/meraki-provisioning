#!/bin/python3
#Kind of a hello world

import requests

BASE_URL = "https://dashboard.meraki.com/api/v0/"
BASE_HEADER = "X-Cisco-Meraki-API-Key: "
KEY = file.open('token').readlines()
CONTENT_TYPE = "Content-Type: application/json"

#currently assuming path has parameters passed in
def request(path):
   url = BASE_URL + path
   headers = { BASE_HEADER : KEY }
   req = requests.get( url, headers=headers )
   return req.json()

def organizations():
   path = "organizations"
   req = request(path)
   print(req)

organizations()
