from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random 

pages = set()
random.seed(datetime.datetime.now())

def getInternalLinks(bsObj,includeUrl):
	includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
	internalLinks = []
	for link in bsObj.findAll("a",href=re.compile("^(/|.*"+includeUrl+")")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in internalLinks:
				if link.attrs['href'].startswith("/"):
					internalLinks.append(includeUrl+link.attrs['href'])
				else:
					internalLinks.append(link.attrs['href'])
	return internalLinks

def getExternalLinks(bsObj,excludeUrl):
	externalLinks=[]
	for link in bsObj.findAll("a",href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in externalLinks:
				externalLinks.append(link.attrs['href'])
	return externalLinks

def splitAddress(address):
	addressParts = address.replace("http://","").split("/")
	return addressParts

def getRandomExternalLink(startingPage):
	print(startingPage)
	try:
		html=urlopen(startingPage)
	except Exception as e:
		print(e)
		return ""
	bsObj = BeautifulSoup(html,'html.parser')
	externalLinks = getExternalLinks(bsObj,urlparse(startingPage).netloc)
	if len(externalLinks)==0:
		print("no externallinks")
		domain=urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc
		internalLinks=getInternalLinks(bsObj,domain)
		return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
	else:
		return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(stratingSite):
	externalLink = getRandomExternalLink(stratingSite)
	print("Random external link is:"+externalLink)
	if len(externalLink)!=0:
		followExternalOnly(externalLink)
	else:
		print("over")

followExternalOnly("http://oreilly.com")
