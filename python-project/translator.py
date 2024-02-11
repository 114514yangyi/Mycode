import requests
import sys
import json
import random


if __name__ == "__main__":
    
    word=sys.argv[1]

    url="https://fanyi.baidu.com/sug"

    headers={
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0"
    }

    data={
        
    }

    data["kw"]=word
    
    with open("/home/huyang/Document/python-project/proxies_pool.json","r") as fp:
        proxies_pool=json.loads(fp.read())
    
    proxies=random.choice(proxies_pool)
    
    print(f"ip-address:{proxies['http']}")


    response=requests.post(url=url,data=data,headers=headers,proxies=proxies)

    response.encoding='utf-8'
    
    content=response.text
    
    obj=json.loads(content)

    result=obj['data']

    for translate in result:
        resultone=translate['v']
        fromone=translate['k']
        output=f"{fromone}->{resultone}"
        print(output)
        