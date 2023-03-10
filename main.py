import scraper.scrape as scrape
import preprocessor as preprocessor

print("\n                 ==================== SEARCH ENGINE ====================\n")
question = input("Search : ")


# assigning weight to find level of the question
question_terms = preprocessor.cleanup_stopwords(question)
print(question_terms)

basic_keywords = ['define', 'list', 'identify', 'describe','who', 'where', 'when', 'what', 'which']
intermediate_keywords = ['compare', 'contrast', 'analyze', 'evaluate','why', 'how']
advanced_keywords = ['critique', 'hypothesize', 'propose', 'explore', 'justify']

score = 0
for word in question_terms:
    if word in basic_keywords:
        score = score + 2
    elif word in intermediate_keywords:
        score = score + 5
    elif word in advanced_keywords:
        score = score + 10
    else: 
        score = score + 1
    


# print("Fetching links for the keyword " + question + "...")
# links = scrape.get_links(question)
# print(links)

# print("Fetching data from the links...")
# content = scrape.get_data(links)
# print("\n")
# print(content)





