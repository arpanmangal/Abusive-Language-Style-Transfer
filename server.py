from flask import Flask, send_from_directory
from app import views

app = Flask(__name__)

## Configuration
app.config.from_object('config.Development')

## API routes
app.add_url_rule('/classify', view_func=views.classify, methods=['POST'])
app.add_url_rule('/convert', view_func=views.convert, methods=['POST'])


## Static Routes ##
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')
