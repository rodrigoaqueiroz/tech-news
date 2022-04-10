from tech_news.analyzer.seach_engine_utils_funcions import (
    get_by_title, get_by_date, get_by_source, get_by_category
)


# Requisito 6
def search_by_title(title):
    get_title = get_by_title(title)
    titles = [(element["title"], element["url"]) for element in get_title]
    return titles


# Requisito 7
def search_by_date(date):
    get_date = get_by_date(date)
    dates = [(element["title"], element["url"]) for element in get_date]
    return dates


# Requisito 8
def search_by_source(source):
    get_source = get_by_source(source)
    sources = [(element["title"], element["url"]) for element in get_source]
    return sources


# Requisito 9
def search_by_category(category):
    get_category = get_by_category(category)
    categories = [
        (element["title"], element["url"]) for element in get_category
    ]
    return categories
