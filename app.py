from flask import Flask

import json
from flask import request
from flask_cors import CORS

import config
from client import LentaClient
from dotenv import load_dotenv


def create_app(config_file=config):
    app = Flask(__name__)
    load_dotenv()
    CORS(app)
    client = LentaClient()

    @app.route('/')
    def live_check():
        return 'App is running'

    @app.route('/news', methods=['GET'])
    def get_news():
        offset = request.args.get('offset') or 0
        limit = request.args.get('limit') or 10
        r = client.list_news(int(offset), int(limit))
        return json.dumps(r, ensure_ascii=False).encode('utf8')

    @app.route('/news-details')
    def get_news_details():
        url = request.args.get('url')
        r = client.parse_news_details(str(url))
        return json.dumps(r, ensure_ascii=False).encode('utf8')

    return app
