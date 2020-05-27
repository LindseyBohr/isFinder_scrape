#!/usr/bin/env python

import time
import re
import urllib.request
from bs4 import BeautifulSoup

#################################################################
### This script scrapes ISFinder search results and grabs the 
### DNA sequence and outputs it to a fasta file 
################################################################

# specify the url
query_page = 'https://isfinder.biotoul.fr/blast/resultat.php?id=phpLyPxKu&title=&prog=blastn'

# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(query_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

outfile = open("query.fasta",'w')

for tag in soup.find_all(href=re.compile('^../scripts/')):
    tempurl = tag['href']
    tempurl = tempurl.split('..')[1]
    tempurl = 'https://isfinder.biotoul.fr/' + tempurl
    page = urllib.request.urlopen(tempurl)
    subsoup = BeautifulSoup(page,'html.parser')
    name = tag['href'].split('=')[1]
    # search for DNA sequence in subsoup
    ptag = subsoup.find('p',string='DNA sequence ')
    dnaTag = ptag.find_next('div')
    dnaTag = re.sub('<.*?>','',str(dnaTag))
    outfile.write('>'+name+'\n')
    outfile.write(dnaTag+'\n')
    print(name)
    time.sleep(1)




outfile.close()





