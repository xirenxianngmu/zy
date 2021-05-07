import random
import re
import time
import os
import requests
import sys





path=sys.path[0]+r'/README.md'
path1=sys.path[0]+r'/历史/memory.md'
cookie =  os.environ["COOKIECH"]
formhash =  os.environ["FORMHASHCH"]
urlz=os.environ["CHURL"]
def q():
    i = ["40", "38", "39", "41", "42", "46", "47", "48", "101"]
    id = random.choice(i)
    url = str(urlz)+"/forum-" + str(id) + "-" + str(
        random.randint(1, 10)) + ".html"
    headers = {
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
        "cookie":cookie
    }
    url0 = str(urlz)+"/k_misign-sign.html?operation=qiandao&format=global_usernav_extra&formhash="+str(formhash)+"&inajax=1&ajaxtarget=k_misign_topb"
    requests.get(url=url0, headers=headers)
    res = requests.get(url=url, headers=headers).text
    c = str(res)
    zz = r'thread-(......)-1-1'
    d = re.findall(zz, c, re.S)
    #去重
    d=list(set(d))
    g = str(random.choice(d))
    url1 = str(urlz)+"/forum.php?mod=viewthread&tid=" + str(g)
    res2 = requests.get(url=url1, headers=headers).text
    zzz = r'postmessage_.+?>(.+?)<'
    q = re.findall(zzz, res2, re.S)
    s = str(random.choice(q)).strip()
    url2 = (
        str(urlz)+"/forum.php?mod=post&action=reply&fid=" +
        str(id) + "&tid=" + str(g) +
        "&extra=&replysubmit=yes&mobile=2&handlekey=fastpost&loc=1&inajax=1")
    headers1 = {
        "user-agent":
        "Mozilla/5.0 (Linux; Android 10; MI 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Mobile Safari/537.36",
        "cookie": cookie,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data1 = {
        "posttime": str(int(time.time())),
        "formhash": formhash,
        "usesig": "1",
        "message": str(s),
    }
    res1 = requests.post(url=url2, headers=headers1, data=data1).text
    print(res1)
    if "成功" in res1:
       z=str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))+':'+'成功了，摸鱼去吧\r\n'
    elif "抱歉" in res1:
       z=str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))+':'+'估摸着又发了些沙雕东西\r\n'
    else:
       z=str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))+':'+'ERROR,快去改代码\r\n'
    with open(path, 'w+') as f:
        f.write(z)
    with open(path1, 'a+') as f:
        f.write(z)


def main_handler(event, context):
    return q()


if __name__ == "__main__":
    q()
