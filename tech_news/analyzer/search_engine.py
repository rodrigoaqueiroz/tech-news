from tech_news.analyzer.seach_engine_utils_funcions import (
    get_by_title, get_by_date, get_by_source
)


# Requisito 6
def search_by_title(title):
    get_title = get_by_title(title)
    titles = [(element["title"], element["url"]) for element in get_title]
    return titles


# Requisito 7
def search_by_date(date):
    get_dates = get_by_date(date)
    dates = [(element["title"], element["url"]) for element in get_dates]
    return dates


# Requisito 8
def search_by_source(source):
    get_source = get_by_source(source)
    sources = [(element["title"], element["url"]) for element in get_source]
    return sources


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
