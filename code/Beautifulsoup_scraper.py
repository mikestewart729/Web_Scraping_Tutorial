## Use beautiful soup for web scraping
## Import statements
from bs4 import BeautifulSoup
from urllib.request import urlopen

## Read in html using urllib, and then convert to a Beautiful Soup object
URL = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(URL)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser") # Use python built in html parser

## First, BeautifulSoup has a get_text method
#print(soup.get_text())

## Beautiful Soup features tag objects for information scraping
## Let's find the image tags
#print(soup.find_all("img")) # View instances of tag objects
image1, image2 = soup.find_all("img")
#print(image1.name) # Name of the tag
print(image1["src"]) # Tag objects have dictionary like attributes
print(image2["src"])
print(soup.title) # Look at the title object. Note how it is "cleaner" than the html
print(soup.title.string) # Look at the title string in the title object

## Beautiful Soup exercise. Use beautiful soup to print out all the links
## on a test page using a specific html tag and then looking for the href attribute
URL = "http://olympus.realpython.org/profiles"
page = urlopen(URL)
html = page.read().decode("utf-8")
#print(html) # Look at the raw html
soup = BeautifulSoup(html, "html.parser")
links = soup.find_all("a")
for link in links:
    print("http:/"+link["href"])