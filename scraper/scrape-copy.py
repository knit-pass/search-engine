# ---------------------------------------------------------------------------- #
#                                   Scrape.py                                  #
# ---------------------------------------------------------------------------- #

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from googlesearch import search
import wikipediaapi


def get_links(keyword, num=10):
    """
    It searches Google for the keyword and returns the top 25 results.

    :param keyword: The keyword you want to search for
    :param num: Number of results per page, defaults to 25 (optional)
    :return: A list of links
    """
    link_results = []
    for j in search(keyword, tld="com", num=num, stop=10, pause=10):
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
    count = 0
    for i in links:
        url = i
        page = ""
        try:
            # Function call to open a page
            page = urlopen(url)
            # Get text content from all the <p> tags from the fetched page
            soup = BeautifulSoup(page, "html.parser")

            content = soup.findAll("p")
            # content = soup.get_text()

            # Join each text snippet to a string then append it to an array
            article = ""
            for i in content:
                article = article + " " + i.text
                article = article + "\n"
            text_content.append(article)
        except:
            continue
    for i in text_content:
        f = open("link" + str(count) + ".txt", "w", encoding="utf-8")
        f.write(i)
        count = count + 1
    return text_content


if __name__ == "__main__":
    print(get_data(get_links("Dog")))
