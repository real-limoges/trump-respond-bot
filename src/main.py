with open('../config/access_token') as f:
    access_token = f.read().strip()

with open('../config/access_secret') as f:
    access_secret = f.read().strip()

with open('../config/consumer_key') as f:
    consumer_key = f.read().strip()

with open('../config/consumer_secret') as f:
    consumer_secret = f.read().strip()


if __name__ == '__main__':
    print "Hello World!"
