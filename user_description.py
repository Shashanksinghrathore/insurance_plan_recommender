import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler

consumer_key = "d3OjrMvopgLYQVz09N2SDrqLa"
consumer_secret = "68fNEgmlIEfZCqkOVv2EGwAm8Kpunkxh6HgHwYrKm4zHdwhn4R"
access_key = "976133803226869760-e5w54HPlOu133IGqoMUZDsvhneazNOm"
access_secret = "MKrnc0JkuqEKRxpjBYb8sHuLiZLW3Bt9rPx2hk6n59toh"

auth = OAuthHandler(consumer_key,consumer_secret)
api = tweepy.API(auth)
auth.set_access_token(access_key,access_secret)

class tweetListener(StreamListener):

    def on_data(self,data):
        print data
        return True
    def on_error(self,status):
        print status

api = tweepy.API(auth)
twitterStream = Stream(auth,tweetListener())
sname = "linkinpark"
#takehandle = api.user_timeline(screen_name = sname)
#test = api.users.lookup(screen_name=sname) 
test = api.lookup_users(user_ids=["#twiter_user_id"])
for user in test:
    print user.screen_name
    print user.name
    print user.description
    print user.followers_count
    print user.statuses_count
    print user.url
    print user.location
    print user.created_at
    print user.geo_enabled
    print user.verified
    print user.time_zone
    
