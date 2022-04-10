from tech_news.database import search_news


def get_by_title(parameter):
    query = search_news({"title": {"$regex": parameter, "$options": "i"}})
    return query

# Referencia:
# https://www.mongodb.com/docs/manual/reference/operator/query/regex/
# To case insensitive
