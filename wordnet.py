# -*- coding: utf-8 -*-

from nltk.corpus import wordnet as wn

acti=wn.synset('activate.v.01')
mut=wn.synset('mutate.v.01')
defi=wn.synset('deficient.a.01')
#print wn.synsets('mutate')
print acti.hypernyms()
print wn.synset('activate.v.01').lowest_common_hypernyms(wn.synset('effect.v.01'))
print acti.path_similarity(defi)
print acti.lch_similarity(mut)
#print acti.wup_similarity(mut)
