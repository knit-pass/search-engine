# ---------------------------------------------------------------------------- #
#                                   Scrape.py                                  #
# ---------------------------------------------------------------------------- #

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
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
    print(link_results)
    return link_results


def get_data(links):
    """
    It takes a list of links, opens each link, fetches the text content from each link, and returns a
    list of text content.

    :param links: A list of links to the articles you want to scrape
    :return: A list of strings.
    """
    text_content = []
    for i in links:
        url = i
        page = ""
        try:
            # Function call to open a page
            page = urlopen(url)
            # Get text content from all the <p> tags from the fetched page
            soup = BeautifulSoup(page, 'html.parser')
            content = soup.findAll('p')
            # Join each text snippet to a string then appeng it to an array
            article = ''
            for i in content:
                article = article + ' ' + i.text
            text_content.append(article)
        except:
            continue
    return text_content


if __name__ == "__main__":
    print(get_data(get_links("Piaget")))
