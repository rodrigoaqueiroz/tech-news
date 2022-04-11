from tech_news.database import get_collection


# Requisito 10
def top_5_news():
    news = get_collection().aggregate([
        {"$project": {
            "_id": 0,
            "title": 1,
            "url": 1,
            "rank_5": {"$sum": ["shares_count", "comments_count"]},
        }},
        {"$sort": {"rank_5": -1, "title": 1}},
        {"$limit": 5},
    ])
    best_ranked_news = [
        (best_ranked["title"], best_ranked["url"]) for best_ranked in news
    ]
    return best_ranked_news


# Requisito 11
def top_5_categories():
    categories = get_collection().aggregate([
        {"$unwind": "$categories"},
        {"$sort": {"categories": 1}},
        {"$limit": 5},
    ])
    best_ranked_categories = [
        best_ranked["categories"] for best_ranked in categories
    ]
    return best_ranked_categories
