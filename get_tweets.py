import tweepy #https://github.com/tweepy/tweepy
import csv


#Twitter API credentials
consumer_key = "d3OjrMvopgLYQVz09N2SDrqLa"
consumer_secret = "68fNEgmlIEfZCqkOVv2EGwAm8Kpunkxh6HgHwYrKm4zHdwhn4R"
access_key = "976133803226869760-e5w54HPlOu133IGqoMUZDsvhneazNOm"
access_secret = "MKrnc0JkuqEKRxpjBYb8sHuLiZLW3Bt9rPx2hk6n59toh"

def get_all_tweets(screen_name, tcount):
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    ntweets = 200
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0 and  ntweets < tcount:
        print "getting tweets before %s" % (oldest)
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        ntweets = ntweets + 200
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        
        print "...%s tweets downloaded so far" % (len(alltweets))
    
    #transform the tweepy tweets into a 2D array that will populate the csv    
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"),tweet.retweet_count,tweet.favorite_count,tweet.coordinates, tweet.geo, tweet.lang, tweet.place, tweet.retweet_count, tweet.source] for tweet in alltweets]
    
    #write the csv    
    with open('%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text","retweet_count","favorite_count","coordinates","geo","lang","place","retweet_count", "source"])
        writer.writerows(outtweets)
        print "Write Completed."
    pass


if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("linkinpark",200)
