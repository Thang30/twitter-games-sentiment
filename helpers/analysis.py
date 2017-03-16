from helpers import settings


def tweet_lengths(text):
    if len(text) < 100:
        return "short"
    elif 100 <= len(text) <= 135:
        return "medium"
    else:
        return "long"


def get_games(row):
    games = []
    text = row["text"].lower()
    for game in settings.GAME_LIST:
        if game in text:
            games.append(game)
    return ",".join(games)
