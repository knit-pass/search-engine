# ---------------------------------------------------------------------------- #
#                                  Process.py                                  #
# ---------------------------------------------------------------------------- #

import nltk
from pywikigraph import WikiGraph
my_loader = WikiGraph.data_root='../py'


def is_noun(pos): return pos[:2] == 'NN'


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

if __name__ == "__main__":
    print(get_concepts("What makes computer better than humans?"))
