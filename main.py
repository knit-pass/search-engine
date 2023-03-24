import scraper
import processor
from utils.logger import Logger
from utils.writer import Writer
from processor import relate

query_links = []


def main():
    # user_query = input()
    # query_links = scraper.get_links(user_query)
    # Logger.write_info("Links fetched")
    # processor.get_readability_report(user_query)
    # Logger.write_info("Readability report created")

    # """
    #     To get the shortest wiki path, use the URL:
    #         https://drive.google.com/drive/folders/1EOv0Lwyt9iH9-2CYW6M7AKvstBvj9IkM?usp=share_link
    #     to download the weights(It's around 1Gb); After downloading, place the files by creating a .pywikigraph directory here.
    # """

    # # wiki_pairs = processor.get_wiki_pairs(user_query)
    # # print("Shortest path: ", processor.get_shortest_path(wiki_pairs[0], wiki_pairs[1]))
    relate.main_relate()


if __name__ == "__main__":
    Logger.start_log()
    main()
    Logger.end_log()
