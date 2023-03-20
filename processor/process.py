# ---------------------------------------------------------------------------- #
#                                  Process.py                                  #
# ---------------------------------------------------------------------------- #
import re
import nltk
from googlesearch import search
# pip install py-readability-metrics
# python -m nltk.downloader punkt
from readability import Readability
import spacy


def flesch_kincaid_index(text):
    text1 = "Quantum computing is a rapidly-emerging technology that harnesses the laws of quantum mechanics to solve problems too complex for classical computers. Today, IBM Quantum makes real quantum hardware -- a tool scientists only began to imagine three decades ago -- available to hundreds of thousands of developers. Our engineers deliver ever-more-powerful superconducting quantum processors at regular intervals, alongside crucial advances in software and quantum-classical orchestration. This work drives toward the quantum computing speed and capacity necessary to change the world.These machines are very different from the classical computers that have been around for more than half a century. Here's a primer on this transformative technology."
    text2 = "On a windy winter morning, a woman looked out of the window.The only thing she saw, a garden. A smile spread across her face as she spotted Maria, her daughter, in the middle of the garden enjoying the weather. It started drizzling. Maria started dancing joyfully.She tried to wave to her daughter, but her elbow was stuck, her arm hurt, her smile turned upside down. Reality came crashing down as the drizzle turned into a storm. Maria's murdered corpse consumed her mind.On a windy winter morning, a woman looked out of the window of her jail cell. this is end of the story"
    r = Readability(text)
    fk = r.flesch_kincaid()
    print(fk.score)
    print(fk.grade_level)


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

def degree_of_separation():
    wg = WikiGraph()
    paths = wg.get_shortest_paths_info('Backpropagation', 'Data Science')
    paths


def depthness(sentence):
    # Load the English language model for spaCy
    nlp = spacy.load("en_core_web_sm")

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


if __name__ == "__main__":
    pass
