import scraper.scrape as scrape

print("==================== SEARCH ENGINE ====================")

search_term = input("Search : ")

print("Fetching links for the keyword " + search_term + "...")
links = scrape.get_links(search_term)
print(links)

print("Fetching data from the links...")
content = scrape.get_data(links)
print("\n")
print(content)