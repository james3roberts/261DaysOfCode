import bs4 as bs
import urllib.request
#place the website i want to scrape here. 
#this web site is for software developer internships with in 25 miles
sauce = urllib.request.urlopen('https://www.indeed.com/jobs?q=software%20developer%20internship&l=Colorado%20Springs%2C%20CO&vjk=0fd925a9df2fc7ee').read()
soup = bs.BeautifulSoup(sauce,'lxml')
#in html the a tag is for a hyperling. This code so far bring up every hyperlink on the page. 
for a in soup.find_all('a'):
    print(a.text)
#now to decide 