# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     train_sql_vec
   Description :
   Author :       ALv
   date：          2020/6/8
-------------------------------------------------
   Change Activity:
                   2020/6/8:
-------------------------------------------------
"""
__author__ = 'ALv'

#python example to train doc2vec model (with or without pre-trained word embeddings)

import gensim.models as g
import logging
import os

#doc2vec parameters
vector_size = 300
window_size = 15
min_count = 1
sampling_threshold = 1e-5
negative_size = 5
train_epoch = 100
dm = 0 #0 = dbow; 1 = dmpv
worker_count = 1 #number of parallel processes

#pretrained word embeddings
pretrained_emb = "toy_data/pretrained_word_embeddings.txt" #None if use without pretrained embeddings

#input sql corpus
sql_raw_path = './toy_data/sql_data/'
sql_file = os.path.join(sql_raw_path,"result.txt")


#output model
saved_path = "toy_data/model.bin"

#enable logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#train doc2vec model
docs = g.doc2vec.TaggedLineDocument(sql_file)
model = g.Doc2Vec(docs, size=vector_size, window=window_size, min_count=min_count, sample=sampling_threshold, workers=worker_count, hs=0, dm=dm, negative=negative_size, dbow_words=1, dm_concat=1, pretrained_emb=pretrained_emb, iter=train_epoch)

#save model
model.save(saved_path)





