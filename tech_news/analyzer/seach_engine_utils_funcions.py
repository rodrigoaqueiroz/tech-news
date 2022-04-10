from tech_news.database import search_news
from datetime import datetime


def get_by_title(parameter):
    query = search_news({"title": {"$regex": parameter, "$options": "i"}})
    return query


def get_by_date(parameter):
    try:
        datetime.strptime(parameter, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    query = search_news({"timestamp": {"$regex": parameter, "$options": "i"}})
    return query

# Referencia:
# https://www.mongodb.com/docs/manual/reference/operator/query/regex/
# To case insensitive
