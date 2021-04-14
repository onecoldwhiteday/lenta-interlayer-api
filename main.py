import json
import os

from flask import Flask, request
from client import LentaClient
from dotenv import load_dotenv

app = Flask(__name__)
client = LentaClient()
load_dotenv()


@app.route('/news', methods=['GET'])
def get_news():
    offset = request.args.get('offset') or 0
    limit = request.args.get('limit') or 10
    r = client.get_overall_news(int(offset), int(limit))
    return json.dumps(r, ensure_ascii=False).encode('utf8')


@app.route('/news-details')
def get_news_details():
    url = request.args.get('url')
    r = client.parse_news_details(os.getenv('BASE_URL') + url)

    return json.dumps(r, ensure_ascii=False).encode('utf8')