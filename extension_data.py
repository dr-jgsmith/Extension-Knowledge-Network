#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 10:37:08 2017

@author: justinsmith
"""

import csv
import time
from random import randrange
from HtmlMapper import HtmlMapper
from clean_html import clean_html

f = open('extension-data.csv', 'w', newline='')
file = csv.writer(f)

x = HtmlMapper(start_url="http://articles.extension.org/")
links = x.get_seed_links() #scrapes all of the links from the page
link_data = x._deep_link_scrape(links)

d1 = []
for i in link_data:
    d1.append(i[0])
    d1.append(i[1])
    dset = sorted(set(d1))
    
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

e_links = []
for i in clean_links:
    if 'extension.org' in i:
        e_links.append(i)
    else:
        pass
        
d2 = []
for i in sorted(set(e_links)):
    link = i
    text = x.get_text_from_link(link)
    clean = clean_html(text)
    row = [link, clean]
    print(row)
    d2.append(row)
    file.writerow(row)
    t = randrange(5)
    time.sleep(t)