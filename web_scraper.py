# Importing urllib.request to get url info
import urllib.request
# Importing beautifulsoup for scraping
from bs4 import BeautifulSoup

# Creating a scraper object that takes a site as parameter.
class Scraper:
    def __init__(self, site):
        self.site = site

    # Scrape function runs urlopen from urllib, on site parameter. saves as 'r'
    def scrape(self):
        r = urllib.request\
            .urlopen(self.site)
        # html is all the html from the r.read() function on the site
        html = r.read()
        # Here, you define that you are parsing html
        parser = "html.parser"
        # Use bs4 to accept the html data and apply the parser.
        sp = BeautifulSoup(html,
                           parser)
        # Now we have all the raw html data. Using a loop, find all instances of <a> in every tag object.
        for tag in sp.find_all("a"):
            # Within the <a> tag, get the href data. assign to url
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)

news = "https://news.yahoo.com/"
Scraper(news).scrape()