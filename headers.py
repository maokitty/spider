import requests
from bs4 import BeautifulSoup

session = requests.session()
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)AppleWebKit 537.36 (KHTML, like Gecko) Chrome","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
url="https://www.whatismybrowser.com/developers/what-http-headers-is-my-browser-sending"
rel=session.get(url,headers=headers)
bsObj = BeautifulSoup(rel.text,'lxml')
# 看了这儿时候没有table返回。。。
print(bsObj)
