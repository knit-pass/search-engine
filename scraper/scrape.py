# ---------------------------------------------------------------------------- #
#                                   Scrape.py                                  #
# ---------------------------------------------------------------------------- #

from googlesearch import search


def get_links(keyword, num=25):
    """
    It searches Google for the keyword and returns the top 25 results.

    :param keyword: The keyword you want to search for
    :param num: Number of results per page, defaults to 25 (optional)
    :return: A list of links
    """
    link_results = []
    for j in search(keyword, tld="com", num=25, stop=25, pause=10):
        link_results.append(j)
    return link_results
