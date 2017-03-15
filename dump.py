import dataset
import helpers.settings as settings

db = dataset.connect(settings.CONNECTION_STRING)

# query all tweet from SQLite database and
# dump them into a .csv file
result = db[settings.TABLE_NAME].all()
dataset.freeze(result=result, format='csv', filename=settings.CSV_NAME)
