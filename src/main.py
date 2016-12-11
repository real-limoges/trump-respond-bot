import tweepy

from DonaldListener import DonaldListener
from auth_config import get_auth

if __name__ == '__main__':
    auth = get_auth()
    donaldListener = DonaldListener()

    tweet_stream = tweepy.Stream(auth=auth, listener=donaldListener)
    tweet_stream.filter(track=['@realdonaldtrump'])
