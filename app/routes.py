import flask
from app import app, db


@app.route('/')
def index():
    return 'Index Page'


@app.route('/news')
def retNews():
    news = db.getNews()

    if not news:
        return []  # "No avaliable tracks"

    newsList = []
    for el in news:
        dict = {
            'id': el[0],
            'userId': el[1],
            'dateStamp': el[2],
            'description': el[3]
        }
        newsList.append(dict)
    return newsList


@app.route('/playgrounds')
def retPlaygrounds():
    playgrounds = db.getPlaygrounds()

    if not playgrounds:
        return []

    playgroundList = []
    for el in playgrounds:
        dict = {
            'id': el[0],
            'name': el[1],
            'geolocation': el[2]
        }
        playgroundList.append(dict)
    return playgroundList
