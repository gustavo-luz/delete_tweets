import tweepy
import keys
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

    message = "Não to crendo, mano.."
    api.update_status(status=message)
    print("Tweeted: %s" % message)