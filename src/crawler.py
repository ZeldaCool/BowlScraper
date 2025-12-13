import requests
from bs4 import BeautifulSoup
import urllib.robotparser
from whoosh.fields import Schema, TEXT, ID, STORED
from whoosh import index
import sys
import os, os.path



def page_scraper():
    global ix
    #add child links in schema
    schema = Schema(raw_html = TEXT(stored=True), 
            text = TEXT(stored=True),)
    print("Enter the website url:")
    url = input()
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        raw_text = soup.get_text()
        print(raw_text)
        b = str(raw_text).encode("utf-8")
        a = str(soup).encode("utf-8")
        pretty_soup = soup.prettify()
        print(pretty_soup)
        if not os.path.exists("indexdir"):
            os.mkdir("indexdir")
        ix = index.create_in("indexdir", schema)
        ix = index.open_dir("indexdir")
        writer = ix.writer()    
        #fix unicode error
        writer.add_document(raw_html = a, text = b)
        writer.commit()

    else:
        print("Error in getting site!")
        sys.exit()

page_scraper()