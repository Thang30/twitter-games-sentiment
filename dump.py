import dataset
import helpers.settings as settings

db = dataset.connect(settings.CONNECTION_STRING)

result = db[settings.TABLE_NAME].all()
dataset.freeze(result=result, format='csv', filename=settings.CSV_NAME)
