try:
    from helpers.private import TWITTER_SECRET, TWITTER_KEY, \
                                                        TWITTER_APP_SECRET, TWITTER_APP_KEY
except Exception:
    pass

CONNECTION_STRING = 'sqlite:///first_tweets.db'
TABLE_NAME = 'zelda_botw'
CSV_NAME = 'zelda_botw.csv'
