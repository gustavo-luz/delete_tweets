import tweepy
#import tweet-delete
import keys

import datetime, json  #Block1
from datetime import datetime, timedelta, timezone

#streamlistener
class MaxListener(tweepy.StreamListener):

    def on_data(self, raw_data):
        self.process_data(raw_data)
        
        return True

    def process_data(self,raw_data):
        print(raw_data)
    
    def on_error(self, status_code):
        if status_code == 420:

            return False

#stream

class MaxStream():

    def __init__(self, auth,listener):
        self.stream =  tweepy.Stream(auth = auth, listener= listener)
        
    def start(self, keyword_list):
        self.stream.filter(track= keyword_list)



if __name__== "__main__":
    listener= MaxListener()
    
    auth = tweepy.OAuthHandler(keys.API_KEY,keys.API_SECRET_KEY)
    auth.set_access_token(keys.ACCESS_TOKEN,keys.ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    stream = MaxStream(auth,listener)
    #cut starting from 1 year ago
    cutoff_date = datetime.now(timezone.utc) - timedelta(days = 365)
    print(cutoff_date)  
    #stream.start(['python'])
    #fp = open("/home/gustavo/python/delete_old_tweets/tweet.json","r", encoding='UTF-8')
    #myjson = json.loads(fp)  #Block 5
    with open("delete_tweets/tweet.json") as f:
        myjson = json.load(f.read())
        #print(myjson[0]['text'])
        
        trash_tweet_ids = [] #Block6
        for tweet in myjson:

            d = datetime.strptime(tweet['tweet']["created_at"], "%a %b %d    %H:%M:%S %z %Y")
            if d < cutoff_date:
                trash_tweet_ids.append(tweet['tweet']['id_str'])
                api.destroy_status(tweet['tweet']['id_str'])
                print(tweet['tweet']["created_at"] + "" + tweet['tweet'] ['id_str'] + ' deleted successfully')
            print(str(len(trash_tweet_ids)) + 'trash tweets have been deleted…')

"""



def oauth_login(consumer_key, consumer_secret):

    
    auth = tweepy.OAuthHandler(keys.API_KEY,keys.API_SECRET_KEY)
    auth_url = auth.get_authorization_url()
    
    verify_code = raw_input("Authenticate at %s and then enter you verification code here > ", auth_url) 
    auth.get_access_token(verify_code)
    
    return tweepy.API(auth)

def batch_delete(api):
    print ("You are about to Delete all tweets from the account @%s." , api.verify_credentials().screen_name)
    print ("Does this sound ok? There is no undo! Type yes to carry out this action.")
    do_delete = raw_input("> ")
    if do_delete.lower() == 'yes':
        for status in tweepy.Cursor(api.user_timeline).items():
            try:
                api.destroy_status(status.id)
                print ("Deleted:", status.id)
            except:
                print ("Failed to delete:", status.id)

if __name__ == "__main__":
    api = oauth_login(keys.API_KEY,keys.API_SECRET_KEY)
    print ("Authenticated as: %s" , api.me().screen_name)
    
    batch_delete(api)

    """