#_*_coding=UTF-8_*_
"""
爬取用js加密的有道词典
"""
from urllib import request, parse

def get_trans(key):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    data = {
    "i": key,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": str(salt),
    "sign": get_sign(key,salt),
    "ts": "1544254981064",
    "bv": "935aa5d04c44a59d6a0ef44faf5e6158",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTIME",
    "typoResult": "false"
    }

    data = parse.urlencode(data).encode()

    header ={
        "Accept": "application/json, text/javascript, */*; q=0.01",
        #"Accept-Encoding": "gzip, deflate",不需要进行压缩
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=1138161526@119.147.183.24; OUTFOX_SEARCH_USER_ID_NCOO=404456851.5747321; JSESSIONID=aaaqxr1oBHdT9cch2WmEw; ___rl__test__cookies=1544254981062",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    req = request.Request(url=url,data=data,headers=header)
    rsp = request.urlopen(req)
    dir = rsp.read().decode()
    print(dir)
    return
    #i = r + parseInt(10 * Math.random(), 10);
    #var t = n.md5(navigator.appVersion),
    #sign: n.md5("fanyideskweb" + e + i + "p09@Bn{h02_BIEe]$P^nG")
def get_salt():
    import time,random
    salt = int(time.time()*1000)+random.randint(0,10)
    return salt
def get_md5(val):
    import hashlib
    md5 = hashlib.md5()
    md5.update(val.encode('utf-8'))
    sign = md5.hexdigest()
    return sign
def get_sign(key,salt):
    sign = "fanyideskweb" + key + str(salt) + "p09@Bn{h02_BIEe]$P^nG"
    sign = get_md5(sign)
    return sign


if __name__ == "__main__":
    salt = get_salt()
    word = input("key_word\n")
    get_trans(str(word))
