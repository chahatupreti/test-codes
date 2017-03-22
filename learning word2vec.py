# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 23:50:17 2016

@author: Krishna
"""

# import modules & set up logging
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
 
sentences = [['first', 'sentence'], ['second', 'sentence']]
# train word2vec on the two sentences
model = gensim.models.Word2Vec(sentences, min_count=1, size=3000)