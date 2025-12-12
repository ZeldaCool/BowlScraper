import requests
from bs4 import BeautifulSoup
import urllib.robotparser
from whoosh.fields import Schema, TEXT, ID, STORED
from whoosh import index
import sys
import os, os.path

def main():
    print("Select format(1,2,3):")
    format = input()
    page_scraper()


def page_scraper():
    global ix
    formatted = input()
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
        raw_text = raw_text.encode("utf-8")
        pretty_soup = soup.prettify()
        print(pretty_soup)
        pretty_soup = pretty_soup.encode("utf-8")
        if not os.path.exists("indexdir"):
            os.mkdir("indexdir")
        ix = index.create_in("indexdir", schema)
        ix = index.open_dir("index")
        writer = ix.writer()    
        writer.add_document(raw_html = pretty_soup, text = raw_text)
        writer.commit()

    else:
        print("Error in getting site!")
        sys.exit()