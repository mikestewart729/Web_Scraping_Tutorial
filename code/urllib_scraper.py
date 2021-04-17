## Start by using built in python functionality and regular expressions to do web scraping
## This notebook will use the built in urllib as well as regex
from urllib.request import urlopen
import re

## Test website set up by RealPython.com
URL = "http://olympus.realpython.org/profiles/aphrodite"

## Open the webpage
page = urlopen(URL)

## Extract th e page information as bytes then decode it
html_bytes = page.read()
html = html_bytes.decode("utf-8") # Use utf-8 encoding to decode the bytes

## Examine the decoded html
#print(html)

## Examine the scraped data using string methods
## For example, find the first occurence of the <title> tag
title_index = html.find("<title>")
#print(title_index)
## Find the start of the page title by passing the title index plus the length of <title>
start_index = title_index + len("<title>")
#print(start_index)
## Get the index of the closing </title> in the same way
closing_index = html.find("</title>")
#print(closing_index)
## Using these indices, slice the html object to find the title
title = html[start_index:closing_index]
#print(title)

## Use an example with messier html to develop intuition for the problems of this approach:
URL = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(URL)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
title_index = html.find("<title>")
start_index = title_index + len("<title>")
closing_index = html.find("</title>")
title = html[start_index:closing_index]
#print(title)
## Note that because the first "<title >" tag has a space after the word title, our
## current approach misses the title tag and returns -1 for the title_index, which leads
## to a strange output for the title after slicing including \n characters, <head> 
## and <title >. Regexes can solve the problem!

## Start to solve the problem by using regular expressions
URL = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(URL)
html = page.read().decode("utf-8") # Method chaining!

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove the html title tags
print(title)

## Exercise: import html from the Dionysus profile and then use .find() to find 
## the text following 'Name:' and 'Favorite color:' not including any leading
## spaces or trailing html tags that might be on the same line
for string in ["Name:", "Favorite Color:"]:
    string_index = html.find(string)
    start_index = string_index + len(string)
    html_tag_index = html[start_index:].find("<")
    end_index = start_index + html_tag_index
    raw_text = html[start_index:end_index]
    clean_text = raw_text.strip(" \r\t\n")
    print(clean_text)

## Can this be done with regular expressions? 
pattern_name = "Name:.*?<"
match_results = re.search(pattern_name, html, re.IGNORECASE)
name = match_results.group()
name = re.sub("Name: ", "", name)
name = re.sub("<", "", name)
print(name)
pattern_color = "Favorite Color:.*?\n"
match_results = re.search(pattern_color, html, re.IGNORECASE)
color = match_results.group()
color = re.sub("Favorite Color: ", "", color)
color = re.sub("\n", "", color)
print(color)