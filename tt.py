#!/usr/bin/env python3
import requests
import sys

TOKEN=sys.argv[3]

r=requests.post("https://botapi.tamtam.chat/messages?access_token={}&chat_id={}".format(TOKEN, sys.argv[1]), 
              json={"text":sys.argv[2]}, 
              headers={"Content-Type": "text/json"})
print(r.status_code)