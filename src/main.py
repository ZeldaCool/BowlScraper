import requests
from bs4 import BeautifulSoup
from flask import Flask
import urllib.robotparser
from whoosh.fields import Schema, TEXT, ID, STORED

def main():
    print("Select format(1,2,3):")
    format = input()

def impolite_scraperformat_one():
    schema = Schema(raw_html = TEXT(stored=True), 
            text = TEXT(stored=True),
            child_links = TEXT(stored=True))
    print("Enter the website url:")
    url = input()
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        
    else:
        print("Error in getting site!")
