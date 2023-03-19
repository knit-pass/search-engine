import requests
from pywikigraph import WikiGraph


def shortest_path_test():
    wg = WikiGraph()
    paths = wg.get_shortest_paths_info("Alan Turing", "Semantic Web")
    print(paths)


def get_nearest_wiki_links(keyword):
    """
    It takes a keyword and returns a list of the top 10 Wikipedia links that are related to that keyword

    :param keyword: The keyword you want to search for
    :return: A list of the top 10 wikipedia links related to the keyword
    """
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {"action": "opensearch", "search": keyword}
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()[1]
    return data


if __name__ == "__main__":
    # shortest_path_test():
    print(get_nearest_wiki_links("Python"))
