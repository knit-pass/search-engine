import spacy
import json
from .wikilinks import *

nlp = spacy.load("en_core_web_lg")
data = {}
digit = 0


def get_data(entity_type):
    try:
        if data[entity_type]:
            return data[entity_type]
    except:
        return []


def insert_to_data(entity, entity_type):
    global data
    try:
        if not data[entity_type]:
            pass
    except:
        data[entity_type] = list()
        data_copy = []
    else:
        data_copy = data[entity_type].copy()
    data[entity_type].append(entity)


def relate_sentence(sentence):
    doc = nlp(sentence)
    data_copy = data.copy()
    for ent in doc.ents:
        insert_to_data(ent.text, ent.label_)
        try:
            relate_with_others(data_copy[ent.label_], ent.text)
        except Exception as e:
            print("Error", e)
            continue


def relate_with_others(items, target):
    global digit
    target_nearest_link = get_nearest_wiki_links(target)
    items_nearest_links = {}
    paths = {}
    for i in items:
        items_nearest_links[i] = get_nearest_wiki_links(i)
    for i in items:
        if not i == target:
            paths[i] = get_shortest_path(
                target_nearest_link[0], items_nearest_links[i][0]
            )
            print("Found for ", i, " ", target)
    j_object = json.dumps(paths, indent=4)
    with open(f"paths{digit}.json", "w") as outfile:
        outfile.write(j_object)
    digit += 1
    print("Data dumped!")


def main_relate():
    s1 = input()
    s2 = input()
    s3 = input()
    relate_sentence(s1)
    relate_sentence(s2)
    relate_sentence(s3)


if __name__ == "__main__":
    s1 = input()
    s2 = input()
    s3 = input()
    relate_sentence(s1)
    relate_sentence(s2)
    relate_sentence(s3)
