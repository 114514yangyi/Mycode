import requests
import json
import random
from lxml import etree
import ddddocr

url="https://so.gushiwen.cn/user/login.aspx?from=http%3A%2F%2Fso.gushiwen.cn%2Fuser%2Fcollect.aspx"

headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0" }

data={
	"__VIEWSTATE": "AGSfL+3yTKGvIGVcCeXv2COdcSvNU/6nQUXHMpPTHMYk/0M5fb8W/ntvE3iwJBeZd+QUfLTv04IIy2sCNJM9bN5fUWjW8kA88h/9g9H/uh1hoPXY0+I2lucM4rOJvu8rCn1ekEUHdTqwDwd8xhuzjWb2+Ys=",
	"__VIEWSTATEGENERATOR": "C93BE1AE",
	"from": "http://so.gushiwen.cn/user/collect.aspx",
	"email": "2416572689huyang@gmail.com",
	"pwd": "114514jK",
	"code": "ptgl",
	"denglu": "登录"
}

with open("proxies_pool.json","r") as  fp:
    proxies_pool=json.load(fp)
    
proxy=random.choice(proxies_pool)

response=requests.get(url=url,headers=headers,proxies=proxy)


response.encoding="utf-8"


content=response.text

tree=etree.HTML(content)

value1=tree.xpath("//input[@id='__VIEWSTATE']/@value")

value2=tree.xpath("//input[@id='__VIEWSTATEGENERATOR']/@value")

data['__VIEWSTATEGENERATOR']=value2[0]

data['__VIEWSTATE']=value1[0]

code_url="https://so.gushiwen.cn"+tree.xpath("//*[@id='imgCode']/@src")[0]

session=requests.session()

code=session.get(url=code_url).content


ocr=ddddocr.DdddOcr()
res=ocr.classification(code)

data["code"]=res

response_post=session.post(url=url,headers=headers,data=data)

with open("down.txt","w",encoding='utf-8') as fp:
    fp.write(response_post.text)
      








        
