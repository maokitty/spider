from urllib.request import urlopen
from bs4 import BeautifulSoup
try:
	html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")	
except HTTPError as e:
	print(e)
else:
	if html is None:
		print("URL not found")
	else:
		#html.parser编译的时候提示的，去掉观察
		bspObj = BeautifulSoup(html.read(),'html.parser')
	print(bspObj.h1)