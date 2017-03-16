import json
import tweepy
import helpers.settings as settings
from textblob import TextBlob
from sqlalchemy.exc import ProgrammingError
import dataset

# set up tweepy to authenticate with Twitter
auth = tweepy.OAuthHandler(settings.TWITTER_APP_KEY,
                           settings.TWITTER_APP_SECRET)
auth.set_access_token(settings.TWITTER_KEY, settings.TWITTER_SECRET)

# pass in the authentication, create an API object to
# pull data from Twitter
api = tweepy.API(auth)

# connect to a SQLite database
db = dataset.connect(settings.CONNECTION_STRING)

# subclass to override methods


class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if status.retweeted:
            return
        # print(status.text)

        description = status.user.description
        loc = status.user.location
        text = status.text
        coords = status.coordinates
        geo = status.geo
        name = status.user.screen_name
        user_created = status.user.created_at
        followers = status.user.followers_count
        id_str = status.id_str
        created = status.created_at
        retweets = status.retweet_count
        bg_color = status.user.profile_background_color

        # get the sentiment score for each tweet
        blob = TextBlob(text)
        sent = blob.sentiment

        # dump geo and coords json dict into string
        if geo is not None:
            geo = json.dumps(geo)

        if coords is not None:
            coords = json.dumps(coords)

        # create a new table in the SQLite database
        table = db[settings.TABLE_NAME]

        # insert information about the tweets
        try:
            table.insert(dict(
                user_description=description,
                user_location=loc,
                coordinates=coords,
                text=text,
                geo=geo,
                user_name=name,
                user_created=user_created,
                user_followers=followers,
                id_str=id_str,
                created=created,
                retweet_count=retweets,
                user_bg_color=bg_color,
                polarity=sent.polarity,
                subjectivity=sent.subjectivity,
            ))
        except ProgrammingError as err:
            print(err)

    def on_error(self, status_code):
        '''Disconnect from Twitter when being rate limited'''
        if status_code == 420:
            return False


stream_listener = StreamListener()
# authentication credentials and calling callback functions
stream = tweepy.Stream(api.auth, listener=stream_listener)
# start streaming with a list of terms to filter on
stream.filter(track=settings.GAME_LIST)
