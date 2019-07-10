 ##### 1、爬虫

```
import requests
import re
import time
import json
import csv
from bs4 import BeautifulSoup

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
s = requests.session()

def write_to_file(info):
    with open("a.txt","a",encoding="utf-8") as f:
        f.write(json.dumps(info,ensure_ascii=False,indent=2))

def get_one_page(url):
    try:
        r=requests.get(url,headers=headers)
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "爬取失败"


def parse_page3(res):
    html = BeautifulSoup(res,"html.parser")
    # print(res)
    result = []
    place = html.select("#list_con > li > div.item_con.job_title > div.job_name.clearfix > a > span.address")
    job = html.select('#list_con > li > div.item_con.job_title > div.job_name.clearfix > a > span.name')
    salary = html.select('#list_con > li > div.item_con.job_title > p')
    company = html.select('#list_con > li > div.item_con.job_comp > div > a')
    welfare = html.select('#list_con > li > div.item_con.job_title > div.job_wel.clearfix')
    for place,job,salary,company,welfare in zip(place,job,salary,company,welfare):
        result.append({
            "place":place.get_text(),
            "job":job.get_text(),
            "salary":salary.get_text(),
            "company":company.get_text(),
            "welfare":welfare.get_text()
            })
    return result

header = ["place","job","salary","company","welfare"]
csvfile = open('data.csv', 'w',newline='')
writer = csv.writer(csvfile)
writer.writerow(header)


def main(offset):
    url="https://hz.58.com/ywtzjingli/pn"+str(offset)+"/?classpolicy=main_null,job_A&final=1&jump=1&PGTID=0d35f8c7-0004-f4fa-d607-70e9d941aa91&ClickID=2"
    html=get_one_page(url)
    result=parse_page3(html)
    print(result)
    tmp1 = []
    for dic in result:
        print(dic)
        tmp=[]
        tmp.append(dic['place'])
        tmp.append(dic['job'])
        tmp.append(dic['salary'])
        tmp.append(dic['company'])
        tmp.append(dic['welfare'])
        print(tmp)
        tmp1.append(tmp)
    writer.writerows(tmp1)

if __name__ == '__main__':
    for i in range(1,4):
        main(i)
        time.sleep(1)
```

![1562757563824](https://github.com/glotozz/task/blob/master/1.png)

##### 2、异步

![1562757352606](https://github.com/glotozz/task/blob/master/2.png)
