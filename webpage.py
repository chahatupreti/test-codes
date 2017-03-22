# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 12:08:56 2016

@author: Krishna
"""

# import re
# import urllib
# from bs4 import BeautifulSoup

# html = urllib.urlopen('http://iitk.ac.in')
# soup = BeautifulSoup(html)
# data = soup.findAll(text=True)

# def visible(element):
#    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
#        return False
#    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
#        return False
#    return True

# result = filter(visible, data)

# print visible_texts

import nltk   
from urllib import urlopen

url = "http://iitk.ac.in"    
html = urlopen(url).read()    
raw = nltk.clean_html(html)  
print(raw)
