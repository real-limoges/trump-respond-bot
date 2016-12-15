import tweepy

from DonaldListener import DonaldListener
from auth_config import get_auth

import time

from requests.packages.urllib3.exceptions import ReadTimeoutError

if __name__ == '__main__':
    auth = get_auth()
    donaldListener = DonaldListener()
    
    tweet_stream = tweepy.Stream(auth=auth, listener=donaldListener)
    #Trump ID - public info
    try:
        tweet_stream.filter(follow=['25073877'])
    except ReadTimeoutError:
        time.sleep(10) 
        tweet_stream.filter(follow=['20573877'])
#    Personal ID - public info
#    tweet_stream.filter(follow=['741352065289486337'])
