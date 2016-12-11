import tweepy


class DonaldListener(tweepy.StreamListener):

    def on_status(self, status):
#        if status.id == 25073877:
#            print status.text
        print status.id, status.text
    def on_error(self, status_code):
        print status_code
        print "https://dev.twitter.com/overview/api/response-codes"
