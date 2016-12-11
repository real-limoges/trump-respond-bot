import tweepy
from pymongo import MongoClient


class DonaldListener(tweepy.StreamListener):
    def on_status(self, status):
        print status 

    def on_error(self, status_code):
        print status_code
        print "https://dev.twitter.com/overview/api/response-codes"
