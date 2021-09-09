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
with open('delete_tweets/tweet.json') as json_file:
    myData = json.load(json_file)

# Range (in UTC offset) within which tweets will be deleted
# =================================================================

range_start = datetime.strptime('Sep 10 00:00:00 +0000 2010','%b %d %H:%M:%S %z %Y')
range_end = datetime.strptime('Sep 10 00:00:00 +0000 2017','%b %d %H:%M:%S %z %Y')

# ==================================================================
# I am creating a list of tweet IDs for consideration, where tweetsToBeDeleted will be
# used for deleting tweet
# ==================================================================

tweetsToBeDeleted = []
tweetsToBeIgnored = []

for element in myData["data"]:
  tweet_post_time = datetime.strptime(element["tweet"]["created_at"],'%a %b %d %H:%M:%S %z %Y')
  if (tweet_post_time>= range_start and tweet_post_time<= range_end ):
    tweetsToBeDeleted.append(element["tweet"]["id_str"])
  else:
    tweetsToBeIgnored.append(element["tweet"]["id_str"])

print(len(tweetsToBeDeleted),len(tweetsToBeIgnored))

for id in tweetsToBeDeleted:
  deleteTweet(id)