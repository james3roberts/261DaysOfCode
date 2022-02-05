#import imp
import requests
from bs4 import BeautifulSoup
from itertools import cycle
import csv

##Going to make proxy so I dont get kicked
##Create a function to call as needed
def getProxies(inURL):
    page = requests.get(inURL)
    soup = BeautifulSoup(page.text,'html.parser')
    terms = soup.find_all('tr')
    IPs = []
    
    for x in range (len(terms)):
        term = str(terms[x])
        if '<tr><td>' in str(terms[x]):
            pos1 = term.find('d>')+2
            pos2 = term.find('</td')
            pos3 = term.find('/td><td>')+9
            pos4 = term.find('</td><td>US<')

            IP = term[pos1:pos2]
            port = term[pos3:pos4]
            if '.' in IP and len(port)<6:
                IPs.append(IP +":"+ port)
                #print(IP +":"+ port)
    return IPs

    #get a proxy to use
    ##using this website to get proxies to use
    proxyURL = "https://www.us-proxy.org/"
    pxs = getProxies(proxyURL)
    ##The proxyPool on a cycle will constantly refresh the proxy for each request
    proxyPool = cycle(pxs)
    ##Make a variable to access the url that we want to go to 
    url = 'https://www.indeed.com/jobs?q=software%20developer%20internship&l=Colorado%20Springs%2C%20CO&vjk=e27d49a4c9e4ffe4'
    page = requests.get (url, proxies = {"http":next(proxypool)})
    soup = BeautifulSoup(page.text, 'html.parser')
    ## so After inspecting the html code it looks like the td tag for indeed is called
    ##id = resultsCol  this has each listing in it 
    ## make a variable to access the actual get the infor from the div tag
    jobs = soup.find(id = 'resultsCol')
    print (jobs)
#time 21:12