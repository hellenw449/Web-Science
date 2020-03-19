"""
Created on Wed Mar  4 17:03:46 2020

@author: Renke Wang 2493604w
"""
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import emoji
 
import twitter_credentials
 
# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """
    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          

    def on_error(self, status):
        print(status)

 
if __name__ == '__main__':
 
    # Authenticate using config.py and connect to Twitter Streaming API.
    hash_tag_list = ['#astonished','#excited','#amused','#excitement','#excite','#exciting','t#hrill','#heat','#passion',
                'happy','delighted','glad','joyful','enjoy','joy','love',
                '#adventure','#enthusiasm','#satisfy','#satisfaction',
                '#pleased','#content','#satisfied','#serene','#pleasant','#calm','#at ease',
               '#surprise','#sad','#frustration','#depressed','#miserable','#gloomy','#distressed',
                    '#disgust','#depression','#fear','#tense','#horrible','#panic','#terror','#fright',
                   '#angry','#afraid','#alarmed','#annoyed','#trash','#shit','#annoy',
                     emoji.emojize(':thumbsup:', use_aliases=True),
                     emoji.emojize(':poop:', use_aliases=True)]
    
    #‘#astonished','#excited','#amused','#excitement','#excite','#exciting','t#hrill','#heat','#passion',
   #                  '#adventure','#enthusiasm','#satisfy','#satisfaction'
   #                  '#pleased','#content','#satisfied','#serene','#pleasant','#calm','#at ease',
   #                  '#surprise','#sad','#frustration','#depressed','#miserable','#gloomy','#distressed',
   #                  '#disgust','#depression','#fear','#tense','#horrible','#panic','#terror','#fright',
   #                  '#angry','#afraid','#alarmed','#annoyed','#trash','#shit','#annoy',
    fetched_tweets_filename = "tweets.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)