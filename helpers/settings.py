try:
    from helpers.private import TWITTER_SECRET, TWITTER_KEY, \
                                                        TWITTER_APP_SECRET, TWITTER_APP_KEY
except Exception:
    pass

CONNECTION_STRING = 'sqlite:///tweets.db'
TABLE_NAME = 'games_tweets'
CSV_NAME = 'games_tweets.csv'
GAME_LIST = ["#BreathOfTheWild", "#shovelknight",
             "#HorizonZeroDawn", "#nierautomata",
             "#nioh", "#nightinthewoods",
             "#ResidentEvil7", "#TormentTidesOfNumenera",
             "#yakuza0", "#hollowknight"]
