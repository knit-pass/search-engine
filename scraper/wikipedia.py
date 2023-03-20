import json
import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia("en")
page_py = wiki_wiki.page("Hockey")
scraped_data = {}


def print_sections(sections, level=0):
    for s in sections:
        scraped_data[s.title] = s.text
        print("%s: %s - %s" % ("*" * (level + 1), s.title, s.text))
        print_sections(s.sections, level + 1)


print_sections(page_py.sections)
j_object = json.dumps(scraped_data, indent=4)
with open("sample.json", "w") as outfile:
    outfile.write(j_object)
