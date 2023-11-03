import joblib
import os
from kiwipiepy import Kiwi

def extract_keywords(filepath, doc, max_sum, mmr, num):
    kiwi = Kiwi()

    if os.path.exists(filepath):
        loaded_model = joblib.load(filepath)
        tokenized_doc = kiwi.analyze(doc)
        tokenized_nouns = ' '.join([i[0] for word in tokenized_doc for i in word[0] if i[1].startswith('NN')])
        keywords_1 = loaded_model.extract_keywords(tokenized_nouns, keyphrase_ngram_range=(num, num), use_maxsum=max_sum, nr_candidates=20, use_mmr=mmr, diversity=0.7, stop_words=None)
        return keywords_1
    else:
        exception_str = "File not present at desired location"
        return exception_str