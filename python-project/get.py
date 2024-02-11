import requests
from lxml import etree
import json
import random
url="https://v1.hitokoto.cn"

headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0" }

fp=open("phrases.txt","w",encoding='utf-8')


for i in range(0,10):
    with open("proxies_pool.json","r") as ff:
        proxies_pool=json.load(ff)
        
    proxies=random.choice(proxies_pool)
    
    response=requests.get(url=url,headers=headers,proxies=proxies)

    content=response.text

    # obj=json.loads(content)
    
    # phrase=obj
    
    print(content)
    # fp.write(f"{phrase[0]}{auther[0]}\n")
    
fp.close()
        