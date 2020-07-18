import json
from nlp import nlp
import pickle
from spacy.tokens import DocBin

def load_inscriptions():
    with open('dbg1.json','r') as f:
        return json.load(f)

def concat_json(corpus):
    """ combines lists into a single string """
    new_corpus = ' '.join(corpus)

    return new_corpus

def pickle_texts(filename,corpus):
    """ pickle the tens of thousands of inscriptions . . . . """

    doc = nlp(corpus)


    with open(f'{filename}.pickle','wb') as f:
        pickle.dump(doc, f)

#    pickle.dump(to_be_pickled, open('save.p','wb'))

def bin_inscriptions(corpus):
    """ put the texts into the docbin """
    doc_bin = DocBin(attrs=["LEMMA","TAG","POS","DEP","HEAD"], store_user_data=True)
    for c in corpus:
        doc = nlp(c)
        doc_bin.add(doc)

    with open('dbg.bin','wb') as f:
        f.write(doc_bin.to_bytes())

if __name__ == '__main__':
    filename = 'andria'
#    with open(f'{filename}.txt','r') as f:
#        corpus = f.read()
    with open(f'{filename}.json','r') as f:
        corpus = json.load(f)
    corpus = concat_json(corpus)
    pickle_texts(filename,corpus)
