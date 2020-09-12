#!flask/bin/python
#initial app from https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
# helping with https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
# NOT WORKING AT ALL
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
        return "Hello, World!"

    if __name__ == '__main__':
            app.run(debug=True)
