#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 13:22:10 2017

@author: justinsmith
extension edge network data
"""

import csv
import networkx as nx
from HtmlMapper import HtmlMapper
import matplotlib.pyplot as plt

f = open('extension-edges.csv', 'w', newline='')
file = csv.writer(f)

x = HtmlMapper(start_url="http://articles.extension.org/")
links = x.get_seed_links() #scrapes all of the links from the page
link_data = x._deep_link_scrape(links)
[file.writerow([i[0], i[1]]) for i in link_data]

G=nx.DiGraph()
G.add_edges_from(link_data)
nx.draw(G)
plt.show()
plt.savefig('circular_graph.png')

nx.draw_random(G)
plt.show()
plt.savefig('random_graph.png')

nx.draw_shell(G)
plt.show()
plt.savefig('shell_graph.png')




