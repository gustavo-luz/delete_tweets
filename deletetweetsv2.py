import sys
import time
from datetime import datetime
import os
import twitter
from dateutil.parser import parse
import numpy as np
import pandas as pd
import json
import keys

# ==================================================================
# API Credentials
# ==================================================================

CONSUMER_KEY = keys.API_KEY
CONSUMER_SECRET = keys.API_SECRET_KEY
ACCESS_TOKEN_KEY = keys.ACCESS_TOKEN 
ACCESS_TOKEN_SECRET = keys.ACCESS_TOKEN_SECRET


api = twitter.Api(consumer_key = CONSUMER_KEY,
                  consumer_secret = CONSUMER_SECRET,
                  access_token_key = ACCESS_TOKEN_KEY,
                  access_token_secret = ACCESS_TOKEN_SECRET)
# ======================================================================================
# Function to delete tweet by ID
# ======================================================================================

def deleteTweet(tweetId):
   try:
     print("Deleting tweet #{0})".format(tweetId))
     api.DestroyStatus(tweetId)
     print("Deleted")

   except Exception as err:
      print("Exception: %s\n" % err)

myData = None
with open('tweet.json') as json_file:
    myData = json.load(json_file)