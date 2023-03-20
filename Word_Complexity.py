import requests
from bs4 import BeautifulSoup
import googlesearch
import wikipedia
import nltk
from nltk.corpus import wordnet
from nltk.corpus import stopwords

wikipedia.set_lang("en")

search_term = input("Enter the search term: ")

search_results = googlesearch.search(search_term, num_results=5)

stop_words = set(stopwords.words('english'))

for url in search_results:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    text = ''
    for paragraph in soup.find_all('p'):
        text += paragraph.text
    
    sentences = nltk.sent_tokenize(text)
    
    def is_complex_word(word):
        if word.isdigit() or word in stop_words:
           return False
        synsets = wordnet.synsets(word)
        if len(synsets) > 0:
            for synset in synsets:
                if synset.pos() in ['a', 's', 'r']:
                    return True
        return False
    
    weights = {}
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        for word in words:
            if is_complex_word(word):
                weights[word] = weights.get(word, 0) + 1
    
    sorted_words = sorted(weights.items(), key=lambda x: x[1], reverse=True)
    
    print(f"\nTop complex words in {url}:")
    for word, weight in sorted_words[:10]:
        print(f"{word}: {weight}")