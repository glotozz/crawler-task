import time
from random import randint
import requests


# 自动填写问卷星
# 绕过服务端限制的方法：使用xff、设置脚本发包的时间间隔
# 目前脚本很大概率会出现国外ip，可以搜集国内ip
url = "https://www.wjx.cn/joinnew/processjq.ashx?submittype=1&curID=43819938&t=1565166732242&starttime=2019%2F8%2F7%2016%3A32%3A09&ktimes=26&rn=606189091.36417905&hlv=1&jqnonce=b636e088-5337-4ff5-973b-4ac2fd8b59ee&jqsign=d050c6%3E%3E%2B3551%2B2%60%603%2B%3F15d%2B2ge4%60b%3Ed3%3Fcc&jpm=17"
for i in range(1,10):
    header = {
        'Host':'www.wjx.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Accept': '* / *',
        'Accept - Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept - Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://www.wjx.cn/jq/43819938.aspx',
        'Content-Length': '32',
        'x-forwarded-for':str(randint(1,255))+','+str(randint(1,255))+','+str(randint(1,255))+','+str(randint(1,255)),
        'Cookie': 'acw_tc=2f624a2a15651667032113449e5a5a78c559be33a29f05393240f389ae1f26; .ASPXANONYMOUS=xwlWYYyD1QEkAAAANGQyY2UwY2QtNmMwMi00YzdjLTkyNjgtYjAwOTJjYzJlZWJhKVHVbWcXUrju0Qwec7aNRZwVtj81; jac43819938=36417905; UM_distinctid=16c6b348da41e1-011e2866b35c748-4c312272-144000-16c6b348da529f; CNZZDATA4478442=cnzz_eid%3D1762370884-1565166375-%26ntime%3D1565166375; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1565166702; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b=1565166729; jpckey=%u5B66%u5386; LastActivityJoin=43819938,103045812444',
        'Connection': 'close'
    }
    print('Using ip:'+header['x-forwarded-for'])

    #submitdata = "1$%s}2$%s}3$%s" % (str(randint(1, 2)), str(randint(1, 4)), str(randint(1, 4)))
    # data = {
    #     'submitdata':submitdata
    # }

    data = "submitdata=1%24"+str(randint(1,2))+"%7D2%24"+str(randint(1,4))+"%7D3%24"+str(randint(1,4))
    print data
    r = requests.post(url,headers=header,data=data)
    print r.headers
    print r.content
    time.sleep(40)