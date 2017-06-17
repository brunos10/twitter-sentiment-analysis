import os
import tweepy
from textblob import textblob
import os


# tutorial: https://www.youtube.com/watch?v=o_OZdbCzHUA

consumer_key = os.environ['TWITTER_API_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_API_CONSUMER_SECRET']

access_token = os.environ['TWITTER_API_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_API_ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Bonomi')

for tweet in public_tweets
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
