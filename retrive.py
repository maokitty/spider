from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import os

def getAbsoluteUrl(baseUrl,source):
	if source.startswith("http://www."):
		url="http://"+source[11:]
	elif source.startswith("http://"):
		url=source
	elif source.startswith("www."):
		url=source[4:]
		url="http://"+source
	else:
		url=baseUrl+"/"+source
	if baseUrl not in url:
		return None
	return url

def getDownloadPath(baseUrl,absoluteUrl,downloadDirectory):
	path= absoluteUrl.replace("www.","")
	path=path.replace(baseUrl,"")
	path=downloadDirectory+path
	directory = os.path.dirname(path)
	if not os.path.exists(directory):
		os.makedirs(directory)
	return path

downloadDirectory = "/Users/liwangchun/Desktop/downloaded"
baseUrl="http://pythonscraping.com"
html=urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html,'html.parser')
downloadedList = bsObj.findAll(src=True)
for downloaded in downloadedList:
	fileUrl = getAbsoluteUrl(baseUrl,downloaded["src"])
	if fileUrl is not None:
		# print(fileUrl)
		urlretrieve(fileUrl,getDownloadPath(baseUrl,fileUrl,downloadDirectory))