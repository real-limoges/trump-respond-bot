# trump-respond-bot

Overview
-----

This bot tweets @realDonaldTrump about his conflicts of interest. Hoping that this bot will gain a little traction to swamp the algorithm that bubbles alt-right individual's tweets.

Implementation
------

This bot uses [tweepy's](http://docs.tweepy.org/) streaming to receive a pulse on @RealDonaldTrump. After doing so, it will respond with a random selection of possible or real conflicts of interest messages.

Due to the way that Twitter releases its streaming data, I have filtered it on @RealDonaldTrump but removed individuals retweeting Trump or tweeting at Trump.

TODO:
---

- Build fault tolerance
- Build messaging
