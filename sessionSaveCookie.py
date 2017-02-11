import requests
# session=requests.Session()
params={'username':'username','password':'password'}
# s=session.post("http://pythonscraping.com/pages/cookies/welcom.php",params)
s=requests.post("http://pythonscraping.com/pages/cookies/welcom.php",params)
print("cookie:")
print(s.cookies.get_dict())
# print(s.cookies.get_dict())
s=requests.get("http://pythonscraping.com/pages/cookies/profile.php",cookies=s.cookies)
# s=session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(s.text)
# 没有用啊。。。是不是没有用cookie了