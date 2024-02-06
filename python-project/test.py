import urllib.request
import 

url="https://ww.jd.com/"

response=urllib.request.urlopen(url)

content=response.read().decode('utf-8')

print(content)
