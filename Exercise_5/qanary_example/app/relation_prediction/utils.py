from nltk import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer  # Bag of Words
from nltk.corpus import stopwords
from nltk import SnowballStemmer
from nltk.stem.snowball import EnglishStemmer
from sklearn.feature_extraction import text  # stopwords
stopWords = text.ENGLISH_STOP_WORDS.union(["book"])  # initialize stopwords
# create stemmer
stemmer = EnglishStemmer()
analyzer = CountVectorizer().build_analyzer()



def stemmed_words(doc):
    return ([stemmer.stem(w) for w in analyzer(doc) if not w in stopWords])
