import bs4 as bs
import urllib.request
#place the website i want to scrape here. 
#this web site is for software developer internships within 25 miles of colorado springs
print('This is the list of Software developer jobs')
sauce = urllib.request.urlopen('https://www.indeed.com/jobs?q=software%20developer%20internship&l=Colorado%20Springs%2C%20CO&vjk=0fd925a9df2fc7ee').read()
soup = bs.BeautifulSoup(sauce,'lxml')
#in html the a tag is for a hyperling. This code so far bring up every hyperlink on the page. 
for a in soup.find_all('a'):
    print(a.text)
#This web site is for software engineer internships within 25 miles of colorado springs
print ('This is the list of software engineer internships')
sauce = urllib.request.urlopen('https://www.indeed.com/jobs?q=software%20engineer%20internship&l=Colorado%20Springs%2C%20CO&vjk=dac4f6720b7c8468').read()
soup = bs.BeautifulSoup(sauce,'lxml')
for a in soup.find_all('a'):
    print(a.text)
#This web site is for web developer internships within 25 miles of colorado springs
print('this is the list of web developer internships ')
sauce = urllib.request.urlopen('https://www.indeed.com/jobs?q=web%20developer%20internship&l=Colorado%20Springs%2C%20CO&vjk=21bf69dadb0ddf2f').read()
soup = bs.BeautifulSoup(sauce,'lxml')
for a in soup.find_all('a'):
    print(a.text)
##Thsi is where I will add some jobs for being an sql developer
print('This is a list of sql developers jobs near me')
sauce = urllib.request.urlopen('https://www.indeed.com/jobs?q=entry%20level%20sql%20developer&l=Colorado%20Springs%2C%20CO').read()
soup = bs.BeautifulSoup(sauce,'lxml')
for a in soup.find_all('a'):
    print(a.text)
##Remote sql jobs because there are no jobs here
print('This is a list of remote sql developer jobs')
sauce = urllib.request.urlopen('https://www.indeed.com/jobs?q=remote%20entry%20level%20sql%20developer&explvl=entry_level&remotejob=032b3046-06a3-4876-8dfd-474eb5e7ed11&vjk=d72e81c61abce539').read()
soup = bs.BeautifulSoup(sauce,'lxml')
for a in soup.find_all('a'):
    print(a.text)
    