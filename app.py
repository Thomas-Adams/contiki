from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
db = SQLAlchemy(app)
ma = Marshmallow(app)



@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login')
def login():
    return ''


if __name__ == '__main__':
    app.run(debug=True)
