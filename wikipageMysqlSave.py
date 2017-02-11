from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import pymysql
conn = pymysql.connect(host="127.0.0.1",unix_socket="/tmp/mysql.sock",user="root",passwd="lwc1029872701",db='mysql',charset='utf8')
cur = conn.cursor()
cur.execute("use wikipedia")
def insertPageIfNotExists(url):
	cur.execute("select * from pages where url=%s",(url))
	if cur.rowcount==0:
		cur.execute("insert into pages(url) values(%s)",(url))
		conn.commit()
		return cur.lastrowid
	else:
		return cur.fetchone()[0]
def insertLink(frompageId,topageId):
	cur.execute("select * from links where frompageId=%s and topageId=%s",(int(frompageId),int(topageId)))
	if cur.rowcount==0:
		cur.execute("insert into links (frompageId,toPageId) values(%s,%s)",(int(frompageId),int(topageId)))
		conn.commit()
pages=set()
def getLinks(pageUrl,recursionLevel):
	global pages
	if recursionLevel>4:
		return
	pageId=insertPageIfNotExists(pageUrl)
	html = urlopen("http://en.wikipedia.org"+pageUrl)
	bsObj=BeautifulSoup(html,'html.parser')
	for link in bsObj.findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
		insertLink(pageId,insertPageIfNotExists(link.attrs['href']))
		if link.attrs['href'] not in pages:
			newpage=link.attrs['href']
			pages.add(newpage)
			getLinks(newpage,recursionLevel+1)
getLinks("/wiki/Kevin_Bacon",0)
cur.close()
conn.close()
