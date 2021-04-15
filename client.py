import os
import feedparser
import requests
from bs4 import BeautifulSoup


class LentaClient:

    @staticmethod
    def list_news(offset, limit):
        news_feed = feedparser.parse(os.getenv('BASE_URL') + '/rss/news')
        result = []
        page_end = offset + limit
        for entry in news_feed.entries[offset:page_end]:
            result.append({
                'title': entry.title,
                'summary': entry.summary,
                'published': entry.published,
                'link': entry.link,
                'image_src': entry.links[1].href
            })
        return result

    @staticmethod
    def parse_news_details(link):
        resp = requests.get(link)
        news_soup = BeautifulSoup(resp.text, "lxml")

        result_content = []

        content = news_soup.select('.b-topic__content .b-text p')
        for c in content:
            result_content.append(c.text) if len(content) > 0 else ''

        image = news_soup.select('.b-topic__title-image .g-picture')
        image = image[0].get('src') if len(image) > 0 else ''

        title = news_soup.select('.b-topic__title')
        title = title[0].text if len(title) > 0 else ''

        return {"title": title, "content": result_content, "image": image}
