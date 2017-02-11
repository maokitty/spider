import requests
params = {'firstname':'R','lastname':'M'}
r = requests.post("http://pythonscraping.com/files/processing.php",data=params)
print(r.text)