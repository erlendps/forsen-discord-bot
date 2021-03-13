# twitch.py

import os
import time

from dotenv import load_dotenv
from twitchAPI.twitch import Twitch
import requests

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

twitch = Twitch(client_id, client_secret)
twitch.authenticate_app([])

TWITCH_STREAM_API_ENDPOINT_V5 = "https://api.twitch.tv/kraken/streams/{}"

API_HEADERS = {
    'Client-ID': client_id,
    'Accept' : 'application/vnd.twitchtv.v5+json',
}

def is_live(user): # returns true of online
    userid = twitch.get_users(logins=[user])['data'][0]['id']
    url = TWITCH_STREAM_API_ENDPOINT_V5.format(userid)

    try:
        req = requests.Session().get(url, headers=API_HEADERS)
        jsondata = req.json()

        if "stream" in jsondata:
            if jsondata["stream"] is not None:
                return True
            
            else:
                return False
    
    except Exception as e:
        print("Error checking user")
        return False


print(is_live("caedrel"))
print(is_live("forsen"))






