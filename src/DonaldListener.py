'''
Sets up the tweepy class listener object for streaming
'''

import tweepy
from auth_config import get_auth


class DonaldListener(tweepy.StreamListener):
    '''
    Creates a donald trump listener. Could be broken into a setup where the
    handle is passed but this project is narrow in scope
    '''
    def on_status(self, status):
        if '@realdonaldtrump' in status.text.encode(
                'ascii', 'ignore').lower().replace(' ', ''):
            pass
        elif status.text.encode(
                'ascii', 'ignore').lower().replace(
                    ' ', '').startswith('rt'):
            pass
        else:
            print status.text
            api = tweepy.API(get_auth())
            api.update_status('testing')

    def on_error(self, status_code):
        print status_code

        # If 420 is returned, kills stream
        if status_code == 420:
            return False
        else:
            print "https://dev.twitter.com/overview/api/response-codes"
