import keys

from twython import Twython
# ==================================================================
# API Credentials
# ==================================================================

CONSUMER_KEY = keys.API_KEY
CONSUMER_SECRET = keys.API_SECRET_KEY
ACCESS_TOKEN_KEY = keys.ACCESS_TOKEN 
ACCESS_TOKEN_SECRET = keys.ACCESS_TOKEN_SECRET

twitter = Twython(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN_KEY,
    ACCESS_TOKEN_SECRET
)

message = "Tweeted from python :D"
twitter.update_status(status=message)
print("Tweeted: %s" % message)