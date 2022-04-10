import re


def get_url(selector):
    url = selector.css("link[rel=canonical]::attr(href)").get()
    return url


def get_title(selector):
    title = selector.css(".tec--article__header__title::text").get()
    return title


def get_timestamp(selector):
    timestamp = selector.css("time::attr(datetime)").get()
    return timestamp


def get_writer(selector):
    writer = selector.css(".tec--author__info *:first-child *::text").get()
    if writer is None:
        writer = selector.css(
          "div.tec--timestamp__item.z--font-bold a::text"
        ).get()
        if writer is None:
            return None
    return writer.strip()


def get_shares_count(selector):
    shares_string = selector.css(".tec--toolbar__item::text").get()
    if shares_string is None:
        return 0
    shares_count = re.sub('[^0-9]', '', shares_string)
    return int(shares_count)
# Referência:
# https://pt.stackoverflow.com/questions/254748/remover-caracteres-n%C3%A3o-num%C3%A9ricos-de-uma-string-em-python


def get_comments_count(selector):
    comment_count = int(selector.css(
      ".tec--btn::attr(data-count)"
    ).get())
    return comment_count


def get_summary(selector):
    summary = "".join(selector.css(
      ".tec--article__body > p:first-child *::text"
    ).getall())
    return summary


def get_sources(selector):
    sources = [element.strip() for element in selector.css(
      "div.z--mb-16 .tec--badge::text"
    ).getall()]
    return sources


def get_categories(selector):
    categories = [element.strip() for element in selector.css(
      "#js-categories a::text"
    ).getall()]
    return categories
