from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is the first flask app running on Render Web Service! live update!'

if __name__ == '__main__':
    app.run()