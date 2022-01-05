import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from typing import *

ONLY_WORDS_PATTERN = r"[a-zA-Z0-9]+"


def tokenize(text: Text, lower=True) -> List[Text]:
    return [w.lower() if lower else w for w in word_tokenize(text)]


def remove_stopwords(words: List[Text], base_stopwords: Set = set(stopwords.words("indonesian")),
                     additional_stopwords: Set = set()) -> List[Text]:
    all_stopwords = set(base_stopwords)
    all_stopwords = all_stopwords.union(additional_stopwords)
    return [w for w in words if w not in all_stopwords]


def keep_only_words(words: List[Text]) -> List[Text]:
    return [w for w in words if re.match(ONLY_WORDS_PATTERN, w)]
