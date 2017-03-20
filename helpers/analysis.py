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
    games_list = [x.lower() for x in settings.GAME_LIST]
    for game in games_list:
        if game in text:
            games.append(game)
    return ",".join(games)
