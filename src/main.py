'''
This module runs the code to setup a twitter stream, create a listener
objet and handle basic exceptions
'''
import time
import tweepy

from DonaldListener import DonaldListener
from auth_config import get_auth

from requests.packages.urllib3.exceptions import ReadTimeoutError

DONALD = '25073877'

if __name__ == '__main__':
    twitter_authorization = get_auth()
    donald_trump_stream = DonaldListener()

    real_time_tweets = tweepy.Stream(
        auth=twitter_authorization,
        listener=donald_trump_stream)

    # Trump ID - public info
    try:
        real_time_tweets.filter(follow=[DONALD])
    except ReadTimeoutError:
        time.sleep(10)
        real_time_tweets.filter(follow=[DONALD])

#    Personal ID - public info
#    tweet_stream.filter(follow=['741352065289486337'])
