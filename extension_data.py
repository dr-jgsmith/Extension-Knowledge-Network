#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 10:37:08 2017

@author: justinsmith
This script provides a rudimentary web crawler and html scrape.

"""

import csv
import time
from random import randrange
from HtmlMapper import HtmlMapper
from clean_html import clean_html

f = open('extension-data.csv', 'w', newline='')
file = csv.writer(f)

#Calling the HtmlMapper class to process a breadth-first web crawl
#In this case we provide a starting url to initiate the crawl.
#The get_seed_links method collects all of the links present in the starting url.
#This provides the seed for collecting links on those pages
x = HtmlMapper(start_url="http://articles.extension.org/")
links = x.get_seed_links() #scrapes all of the links from the page
link_data = x._deep_link_scrape(links)

#The _deep_link_scrape returns an edge list, so we need to flatten the two lists and combine them as a single sorted set.
d1 = []
for i in link_data:
    d1.append(i[0])
    d1.append(i[1])
    dset = sorted(set(d1))

#Due to limitations of the current code, we need to clean extra forward slashes appended to the link.
clean_links = []
for i in dset:
    a = list(i)
    b = len(a) - 2
    c = a[b:]
    d = ''.join(c)
    if d == "//":
        b = len(a) - 1
        c = a[:b]
        print(''.join(c))
        clean_links.append(''.join(c))
    else:
        print(i)
        clean_links.append(i)

#Since this output cleans all links, we can end up with a very large list. 
#So we will isolate only those links that include our target domain.
e_links = []
for i in clean_links:
    if 'extension.org' in i:
        e_links.append(i)
    else:
        pass
#Create csv document for later analysis      
for i in sorted(set(e_links)):
    link = i
    text = x.get_text_from_link(link) #this method does exactly what it is called.
    clean = clean_html(text) #Strip the html from the returned document
    row = [link, clean]
    file.writerow(row) #Write this data
    t = randrange(5)
    time.sleep(t)
