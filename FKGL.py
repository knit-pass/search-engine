import requests
from bs4 import BeautifulSoup
import textstat

search_term = input("Enter search term: ")

google_url = "https://www.google.com/search?q=" + search_term + "&num=5"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

response = requests.get(google_url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

search_results = []
for i in range(5):
    search_result = soup.select('div.yuRUbf > a')[i]['href']
    search_results.append(search_result)

for i, url in enumerate(search_results):

    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    paragraphs = soup.find_all('p')

    for j, p in enumerate(paragraphs):
        fkgl_score = textstat.flesch_kincaid_grade(p.text)
        print("FKGL score for paragraph ", i+1, ".", j+1, " on ", url, ": ", fkgl_score)
