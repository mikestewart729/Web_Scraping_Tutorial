import mechanicalsoup
import time

## Interact with a webpage that rolls a dice every time the browser is refreshed
browser = mechanicalsoup.Browser()
#page = browser.get("http://olympus.realpython.org/dice")
#tag = page.soup.select("#result")[0]
#result = tag.text
#print(f"The result of your dice roll is {result}")

## Show how time module works
#print("I'm about to wait for five seconds...")
#time.sleep(5)
#print("Done waiting!")

## Combine the time module with mechanical soup
for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"The result of your dice roll is {result}")
    if i < 3: # Don't wait on last iteration, otherwise
        time.sleep(10) # Wait ten seconds and then refresh the headless browser
