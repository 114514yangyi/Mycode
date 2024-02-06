import urllib.request
import urllib.parse
import json
import random
from bs4 import BeautifulSoup



url="https://www.kuaidaili.com/free/intr/"

headers={
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0"
}



request=urllib.request.Request(url=url,headers=headers)

response=urllib.request.urlopen(request)

content:str=response.read().decode("utf-8")

with open("proxies_pool.json","w",encoding='utf-8') as fp:
    soup = BeautifulSoup(content, 'html.parser')
    result_ip=soup.find_all("td",attrs={"data-title":"IP"})
    result_port=soup.find_all('td',attrs={"data-title":"PORT"})
    result=[f"{element[0].text}:{element[1].text}" for element in zip(result_ip,result_port)]
    proxies_pool=[{"http": element} for element in result]
    json.dump(proxies_pool,fp)
        
    





