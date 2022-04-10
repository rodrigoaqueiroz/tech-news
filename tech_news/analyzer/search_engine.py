from tech_news.analyzer.seach_engine_utils_funcions import get_by_title


# Requisito 6
def search_by_title(title):
    get_title = get_by_title(title)
    titles = [(element["title"], element["url"]) for element in get_title]
    return titles


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
