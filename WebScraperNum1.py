import imp
import requests
from bs4 import BeautifulSoup
from itertools import cycle
import csv

##Going to make proxy so I dont get kicked
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
    proxyURL = "https://www.us-proxy.org/"
    pxs = getProxies(proxyURL)
    proxyPool = cycle(pxs)
    ##time is 10:46