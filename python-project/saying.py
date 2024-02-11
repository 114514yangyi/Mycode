import requests
import json
import random

url="https://v1.hitokoto.cn/"

headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0" }

with open("proxies_pool.json","r") as  fp:
    proxies_pool=json.load(fp)
    proxies=random.choice(proxies_pool)
    

response=requests.get(url=url,headers=headers)

content=response.json()


print(f"{content['hitokoto']}       ----{content['from']}")

