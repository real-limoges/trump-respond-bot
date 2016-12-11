import tweepy

from DonaldListener import DonaldListener
from auth_config import get_auth

if __name__ == '__main__':
    auth = get_auth()
    donaldListener = DonaldListener()

    tweet_stream = tweepy.Stream(auth=auth, listener=donaldListener)
    #Trump ID - public info
    tweet_stream.filter(follow=['25073877'])
    #Personal ID - public info
#    tweet_stream.filter(follow=['741352065289486337'])
