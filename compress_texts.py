import json
from nlp import nlp
import pickle
from spacy.tokens import DocBin

def load_txt(infile):
    with open(infile,'r') as f:
        return f.read()

def load_json(infile):
    with open(infile,'r') as f:
        return json.load(f)

def concat_json(corpus):
    """ combines lists into a single string """
    new_corpus = ' '.join(corpus)

    return new_corpus

def pickle_texts(outfile,text):
    """ pickle the tens of thousands of inscriptions . . . . """

    doc = nlp(text)


    with open(outfile,'wb') as f:
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
    infile = 'ap_readings.txt'
    outfile = 'Barrel/ap_readings.pickle'
#    with open(f'{filename}.txt','r') as f:
#        corpus = f.read()
    text = load_txt(infile)
    pickle_texts(outfile,text)
