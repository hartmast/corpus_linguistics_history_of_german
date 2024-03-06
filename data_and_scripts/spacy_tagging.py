# install spacy:
# in terminal: pip install spacy

# install German language model:
# in terminal: pip install https://github.com/explosion/spacy-models/releases/download/de_core_news_sm-3.7.0/de_core_news_sm-3.7.0.tar.gz

import spacy
import pandas as pd
import itertools
import os
import numpy
# nltk.download("averaged_perceptron_tagger")

# list files
root = "/Users/stefanhartmann/sciebo/Projekte/Turin2024/data_and_scripts/postillon_files/"
f = os.listdir("postillon_files")

# get absolute file paths:
for i in range(len(f)):
    f[i] = os.path.join(root, f[i])


# load model
nlp = spacy.load("de_core_news_sm")

# read all files:
d = []

for i in range(len(f)):
    fl = open(f[i], "r")
    d.append(fl.readlines())


# iterate over all items:
for j in range(len(d)):
    
    # tag current tweet
    cur = nlp(str(d[j]))      

    # collectors for pos and lemma
    toks = []
    pos = []
    lemma = []

    # get lemma and pos lists
    for tok in cur:
        toks.append(tok)
        lemma.append(tok.lemma_)
        pos.append(tok.pos_)
        
    # repeat id as often as necessary
    cur_id = list(itertools.repeat(j, len(toks)))

    # combine everything into a dataframe
    cur_df = pd.DataFrame(data = {'tok': toks,
                              'lemma': lemma,
                              'pos': pos,
                              'id': cur_id

    })

    # add to previous dataframe
    if(j == 0):
        all_df = cur_df
    else:
        all_df = all_df._append(cur_df)

    print(j)


all_df.to_csv("postillon_tagged.csv")








