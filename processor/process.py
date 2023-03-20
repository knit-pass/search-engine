# ---------------------------------------------------------------------------- #
#                                  Process.py                                  #
# ---------------------------------------------------------------------------- #
import re
import nltk
import spacy
from prettytable import PrettyTable
from spacy_readability import Readability
from googlesearch import search
from nltk.corpus import stopwords
from .wikilinks import *

nlp = spacy.load("en")
nlp.add_pipe(Readability())


def cleanup_stopwords(s):
    """
    It takes a string as input, tokenizes it, removes stopwords, and returns a list of tokens

    :param s: The string to be cleaned up
    :return: A list of words that are not stopwords and are longer than 2 characters.
    """
    required = ["who", "where", "when", "why", "what", "which", "how"]
    stopset = set(stopwords.words("english")) - set(required)
    tokens = nltk.word_tokenize(s)
    cleanup = [
        token.lower()
        for token in tokens
        if token.lower() not in stopset and len(token) > 2
    ]
    return cleanup


def get_indices(text):
    """
    It takes a string of text, runs it through the spaCy pipeline, and returns a dictionary of
    readability scores

    :param text: The text to be analyzed
    :return: A dictionary with the keys being the name of the readability index and the values being the
    readability index score.
    """
    doc = nlp(text)
    indices = {
        "fk_grade": round(doc._.flesch_kincaid_grade_level, 2),
        "fk_readability": round(doc._.flesch_kincaid_reading_ease, 2),
        "dale_chall": round(doc._.dale_chall, 2),
        "smog": round(doc._.smog, 2),
        "cl_index": round(doc._.coleman_liau_index, 2),
        "ar_index": round(doc._.automated_readability_index, 2),
        "forcast": round(doc._.forcast, 2),
    }
    return indices


def is_noun(pos):
    return pos[:2] == "NN"


def get_concepts(sentence):
    """
    - Tokenize the sentence into words
    - Filter the words to only include nouns
    - Return the nouns

    :param sentence: The sentence to be analyzed
    :return: A list of nouns
    """
    tokenized = nltk.word_tokenize(sentence)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
    return nouns


def degree_of_separation(source, destination):
    """
    It takes two Wikipedia page titles as input, and returns the shortest path between them

    :param source: The source node
    :param destination: The destination page
    :return: The shortest path between the source and destination.
    """
    wg = WikiGraph()
    paths = wg.get_shortest_paths_info(source, destination)
    return paths


def depthness(sentence):
    """
    It takes a sentence, parses it with spaCy, and then counts the depth of each token in the sentence

    :param sentence: The sentence to parse
    """
    # Parse the sentence using spaCy's dependency parser
    doc = nlp(sentence)

    # Define a function to recursively count the depth of a token
    def count_depth(token):
        # If the token has no children, return 0
        if not list(token.children):
            return 0
        # Otherwise, recursively count the depth of each child
        else:
            child_depths = [count_depth(child) for child in token.children]
            # Return the maximum child depth, plus 1 for the current token
            return max(child_depths) + 1

    # Find the depth of each token in the sentence
    depths = [count_depth(token) for token in doc]

    # Print the depth of each token
    for token, depth in zip(doc, depths):
        print(f"{token.text}: {depth}")


def analyze_question(question):
    question_terms = cleanup_stopwords(question)
    print(question_terms)

    basic_keywords = [
        "define",
        "list",
        "identify",
        "describe",
        "who",
        "where",
        "when",
        "what",
        "which",
    ]
    intermediate_keywords = ["compare", "contrast", "analyze", "evaluate", "why", "how"]
    advanced_keywords = ["critique", "hypothesize", "propose", "explore", "justify"]

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
    print("Weightage of the question = " + str(score))


def get_readability_report(sentence):
    """
    It takes a sentence as input, and returns a table with the readability indices for that sentence

    :param sentence: The sentence you want to analyze
    """
    x = PrettyTable()
    print("\n")
    print("Sentence: ", sentence)
    x.field_names = ["Index", "Value"]
    indices = get_indices(sentence)
    x.add_row(["Flesch-Kincaid Grade", indices["fk_grade"]])
    x.add_row(["Flesch-Kincaid Readability", indices["fk_readability"]])
    x.add_row(["Dale Chall", indices["dale_chall"]])
    x.add_row(["Smog", indices["smog"]])
    x.add_row(["Coleman Liau Index,", indices["cl_index"]])
    x.add_row(["Automated Readability Index,", indices["ar_index"]])
    x.align = "l"
    print(x)
    print("\n")
    print("\n")


def get_wiki_pairs(query):
    concepts = get_concepts(query)
    wiki_pages = []
    for i in concepts:
        wiki_pages.append(get_nearest_wiki_links(i)[0])
    return wiki_pages


if __name__ == "__main__":
    get_readability_report("What is a computer?")
    get_readability_report("How can artifical intelligence improve lives?")
    pass
