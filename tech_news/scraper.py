import requests
import time
from parsel import Selector


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
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
