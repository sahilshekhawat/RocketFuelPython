import requests
from bs4 import BeautifulSoup
import re


url_base = 'http://ipinfo.io/'
as_base = 'AS'
ASes = []
f = open('ASes', 'r')
for line in f.readlines():
    ASes.append(line.rstrip())


# with open('ASes', 'r') as f:
#     for asn in f.readlines():
for asn in ASes:
    asn = asn.rstrip('\n')
    output = open('Prefix/AS'+asn, 'w')
    ASN = as_base + asn
    page = requests.get(url_base+ASN)
    html_doc = page.content
    soup = BeautifulSoup(html_doc, 'html.parser')
    #print soup
    for link in soup.find_all('a'):
        if asn in link.get('href'):
            auxstring = '/'+as_base+asn+'/'
            line = re.sub(auxstring, '', link.get('href'))
            printstring = line+'\n'
            if 'AS' not in printstring:
                output.write(printstring)
    print "Running for: " + str(asn)

print 'script finished'
