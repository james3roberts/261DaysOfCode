##Going to make a webScraper in python using beautiful soup 4
from urllib.request import urlopen
from bs4 import BeautifulSoup

urlToScrape="https://www.internships.com/app/search?keywords=&position-types=internship&location=colorado+Spring+colorad&context=seo&seo-mcid=-1"
requestPage=urlopen(urlToScrape)
pageHtml = requestPage.read()
requestPage.close()
