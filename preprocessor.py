import nltk
# nltk.download("stopwords")      #run this once
from nltk.corpus import stopwords


def cleanup_stopwords(s):
    required = ['who', 'where', 'when', 'why', 'what', 'which', 'how']
    stopset = set(stopwords.words('english')) - set(required)
    tokens = nltk.word_tokenize(s)
    cleanup = [token.lower()for token in tokens if token.lower()
               not in stopset and len(token) > 2]
    return cleanup
