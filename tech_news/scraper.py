import requests
import time
from parsel import Selector
from tech_news.scrape_noticias_functions import (
    get_url, get_title, get_timestamp,
    get_writer, get_shares_count, get_comments_count,
    get_summary, get_sources, get_categories
)
# from tech_news.database import create_news


def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        response = None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    url_links = selector.css(".tec--card__info h3 a::attr(href)").getall()
    return url_links

# 'If there are no matches, None is returned.'
# Doc: https://parsel.readthedocs.io/en/latest/usage.html


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_url = selector.css(".tec--list__item ~ a::attr(href)").get()
    return next_page_url


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    result = {
        "url": get_url(selector),
        "title": get_title(selector),
        "timestamp": get_timestamp(selector),
        "writer": get_writer(selector),
        "shares_count": get_shares_count(selector),
        "comments_count": get_comments_count(selector),
        "summary": get_summary(selector),
        "sources": get_sources(selector),
        "categories": get_categories(selector),
    }
    return result


# Requisito 5
def get_tech_news(amount):
    # url = 'https://www.tecmundo.com.br/novidades'
    news_amount = amount
    return news_amount
# url = 'https://www.tecmundo.com.br/novidades'
