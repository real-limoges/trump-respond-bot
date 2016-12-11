import tweepy


class DonaldListener(tweepy.StreamListener):

    def on_status(self, status):
        if '@realdonaldtrump' in status.text.encode('ascii', 'ignore').lower().replace(' ',''):
            pass
        else:
            print status.text

    def on_error(self, status_code):
        print status_code

        # If 420 is returned, kills stream
        if status_code == 420:
            return False
        else:
            print "https://dev.twitter.com/overview/api/response-codes"
