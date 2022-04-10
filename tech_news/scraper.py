import requests
import time
from parsel import Selector
import re


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
   
    def get_writer():
        writer = selector.css(".tec--author__info *:first-child *::text").get()
        if writer is None:
            writer = selector.css("div.tec--timestamp__item.z--font-bold a::text").get()
            if writer is None:
                return None
        return writer.strip()

    def get_shares_count():
        shares_string = selector.css(".tec--toolbar__item::text").get()
        if shares_string is None:
            return 0
        shares_count = re.sub('[^0-9]', '', shares_string)
        return int(shares_count)
    # Referência: https://pt.stackoverflow.com/questions/254748/remover-caracteres-n%C3%A3o-num%C3%A9ricos-de-uma-string-em-python     

    result = {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css(".tec--article__header__title::text").get(),
        "timestamp": selector.css("time::attr(datetime)").get(),
        "writer": get_writer(),
        "shares_count": get_shares_count(),
        "comments_count": int(selector.css(".tec--btn::attr(data-count)").get()),
        "summary": "".join(selector.css(".tec--article__body > p:first-child *::text").getall()),
        "sources": [element.strip() for element in selector.css("div.z--mb-16 .tec--badge::text").getall()],
        "categories": [element.strip() for element in selector.css("#js-categories a::text").getall()],
    }
    return result


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""




html = fetch('https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm')
# print(scrape_noticia(html))
print(scrape_noticia(html))
