import mechanicalsoup
browser = mechanicalsoup.Browser() # Create a Headless web browser object

URL = "http://olympus.realpython.org/login"
page = browser.get(URL) # Request page from the Internet
#print(page) # Result is a  response object

#print(type(page.soup)) # page has a BeautifulSoup object .soup
#print(page.soup)

## Knowing the underlying structure of the page, let's try to login!
login_page = browser.get(URL)
login_html = login_page.soup

form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus" # We know the username and password
form.select("input")[1]["value"] = "ThunderDude"

profiles_page = browser.submit(form, login_page.url) # Submit the form
#print(profiles_page.url) # Check that we have logged in correctly

## Get all the links from the profiles page once logged in
base_url = "http://olympus.realpython.org"
links = profiles_page.soup.select("a")
for link in links:
    address = base_url + link["href"]
    text = link.text
    print(f"{text}: {address}")