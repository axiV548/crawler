# -*- coding: utf-8 -*-
import requests
import json
import time
import pdfkit


key = ''

def wx(offset,key):
    wenzhang = []
    headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Mobile Safari/537.36'}
    url = "https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=Mzg4NzA3OTQzMQ==&f=json&offset=" + str(offset) +"&count=10&is_ok=1&scene=124&uin=MTk1MTgwOTM4Ng%3D%3D&key=" + key + "&pass_ticket=xBlYUoQKFKD%2FBdbTYRt5F%2Fgp15rtp%2FWILa%2Fjb%2BzsAPoF%2BRK175RfwI3H6DWKwerL&wxtoken=&appmsg_token=1056_1gXxCGtGYTFxgvvN785T3RMwVfJdplMWpXNVYQ~~&x5=0&f=json%20HTTP/1.1"
    html = requests.get(url, headers=headers).text
    print(url)
    jsons = json.loads(html)       
    print(jsons)
    if jsons['can_msg_continue']:
        general_msg_list = json.loads(jsons['general_msg_list'])
        print(general_msg_list["list"])
        for y in general_msg_list['list']:
            dd = {}
            list = y['app_msg_ext_info']
            print('list', list)
            title = list['title']
            content_url = list['content_url']
            # print(title, content_url, cover)
            dd['title'] = title
            dd['content_url'] = content_url
            wenzhang.append(dd)
            for x in list['multi_app_msg_item_list']:
                dd = {}
                title_min = x['title']
                content_url_min = x['content_url']
                # print(title_min, content_url_min, cover_min)
                dd['title_min'] = title_min
                dd['content_url_min'] = content_url_min
        return wenzhang

lists = []
for offset in range(10, 100, 10):
    lists.append(wx(offset, key))

# print(lists)
#{'title': '“天眼”助力农村生活垃圾治理  发现的3300余处乱堆乱放点均及时清理', 'content_url': 'http://mp.weixin.qq.com/s?__biz=Mzg4NzA3OTQzMQ==&amp;mid=2247487812&amp;idx=1&amp;sn=6a13fcda4d9a95836e8e7e32a7cdbea2&amp;chksm=cf8e862cf8f90f3a90ae3fc52261a596a7555841c538660232a6480dd9dd86e25ad4296b11c7&amp;scene=27#wechat_redirect', 'cover': 'http://mmbiz.qpic.cn/mmbiz_png/qEaZSLMQqa2wXjkCfRcpfz6nEFShL5eXy6qabqYY0GDMS6NXteydE9uzluKgTpH5NPulCl676t55fj6XaXjrZg/0?wx_fmt=png'}, {'title': '农业农村部农村社会事业促进司副司长何斌：乡村也要开启“美颜”模式', 'content_url': 'http://mp.weixin.qq.com/s?__biz=Mzg4NzA3OTQzMQ==&amp;mid=2247487806&amp;idx=1&amp;sn=6f54a9851ae75dbadd34bead5cde671d&amp;chksm=cf8e8656f8f90f4095e46d4ff3a8e86b26eff7b2451826c708aad74213654a3a35728a0d16a2&amp;scene=27#wechat_redirect', 'cover': 'http://mmbiz.qpic.cn/mmbiz_jpg/qEaZSLMQqa2wXjkCfRcpfz6nEFShL5eXu4VrOU87amzicDkuqn1qqgbkWibqZp8iavMyJAPEzxzAcxqX59lrpv9fA/0?wx_fmt=jpeg'}, {'title': '海南：“三抓三促”高效改善人居环境', 'content_url': 'http://mp.weixin.qq.com/s?__biz=Mzg4NzA3OTQzMQ==&amp;mid=2247487788&amp;idx=1&amp;sn=0c60d7371d445a5d08d953c97a503cc3&amp;chksm=cf8e8644f8f90f523a47a566925bfad28fc7234ff29a021aefdc0353bb2bf681dcc39626aac8&amp;scene=27#wechat_redirect', 'cover': 'http://mmbiz.qpic.cn/mmbiz_jpg/qEaZSLMQqa3b4USZ0diaKmNQWV6LAmJZw4ChPSPAyiavIguqoicXBmJ28G3IMFLDv6lyD0fp9yIHrSrWA86egUY9A/0?wx_fmt=jpeg'}, {'title': '关于开展第32个爱国卫生月活动 为全面打赢新冠肺炎疫情阻击战营造良好环境的通知', 'content_url': 'http://mp.weixin.qq.com/s?__biz=Mzg4NzA3OTQzMQ==&amp;mid=2247487767&amp;idx=1&amp;sn=a9716080879481fe88ee0eef4d40f2fc&amp;chksm=cf8e867ff8f90f697502557f737f2d1d9fd1f5aa26e99e676819d05aec935c5314568be41026&amp;scene=27#wechat_redirect', 'cover': 'http://mmbiz.qpic.cn/mmbiz_jpg/qEaZSLMQqa0IwyJwIiaaMEhftkH7AnIlu4NlHWXyvRmjDfX4LpSjgzanIYVIeJGeTEhMCmLc5sP6PWXbFBzoDeQ/0?wx_fmt=jpeg'}, {'title': '人民日报刊文：打牢基础，美丽乡村更宜居', 'content_url': 'http://mp.weixin.qq.com/s?__biz=Mzg4NzA3OTQzMQ==&amp;mid=2247487765&amp;idx=1&amp;sn=0b21d4ff0cb1108127c8315182d75097&amp;chksm=cf8e867df8f90f6b52aa19d9c593fc291cc79621177e3349b555b6de78aa5618ba63c2dad7b6&amp;scene=27#wechat_redirect', 'cover': 'http://mmbiz.qpic.cn/mmbiz_jpg/qEaZSLMQqa0IwyJwIiaaMEhftkH7AnIlu0urq1B6iaLlicdI3ZF1tsVl9LfuCU5ib5bvoBGqDMapT0W4IsPFKOIEDA/0?wx_fmt=jpeg'}, {'title': '乡村秀美\u3000青春建功——全国共青团系统参与农村人居环境整治扫描', 'content_url': 'http://mp.weixin.qq.com/s?__biz=Mzg4NzA3OTQzMQ==&amp;mid=2247487710&amp;idx=1&amp;sn=65fc7c5b5e89eb5267e002b6c27f58d9&amp;chksm=cf8e87b6f8f90ea02e97005014be68d9a01abf13efd009c50b0bc83681ca3b3ae399713bc397&amp;scene=27#wechat_redirect', 'cover': 'http://mmbiz.qpic.cn/mmbiz_jpg/qEaZSLMQqa0rmv4e3Df6ice6ohtTe68auNhursFeucQvluPKdDjlY2UvJ71qKibR1W04ib204DnFZxVB31soIpfng/0?wx_fmt=jpeg'}, {'title': '农业农村部等6部门关于抓好大检查发现问题整改扎实推进农村人居环境整治的通知', 'content_url': 'http://mp.weixin.qq.com/s?__biz=Mzg4NzA3OTQzMQ==&amp;mid=2247487685&amp;idx=1&amp;sn=917f75929364893422b04e78bc6918d8&amp;chksm=cf8e87adf8f90ebb1710294f4d4d2933562f734c056176fab7640d0d1e7bd4e82b8e689531b3&amp;scene=27#wechat_redirect', 'cover': 'http://mmbiz.qpic.cn/mmbiz_jpg/qEaZSLMQqa06BzVRJQzlPAk1WEXriaaRDf6sdZsEA8QhJZT6Q1iagghvRtXDCTkarRVzdib4aPicKTlzBOO7iafgAqg/0?wx_fmt=jpeg'}, {'title': '统筹推进疫情防控和“三农”工作 补上全面小康“三农”领域短板', 'content_url': 'http://mp.weixin.qq.com/s?__biz=Mzg4NzA3OTQzMQ==&amp;mid=2247487657&amp;idx=1&amp;sn=dc79840cead717fe75d1e4a1b4f7a6af&amp;chksm=cf8e87c1f8f90ed795e1bfd2cb557368a9675d9e1e698b2c43182485e753869301d857c4b33b&amp;scene=27#wechat_redirect', 'cover': 'http://mmbiz.qpic.cn/mmbiz_jpg/qEaZSLMQqa09LSu3rpce3kUgn4JmTTkMHT6VQB7ibDicy0hp5UwzN7fm60NOLSNC5SJdKk1vfRGPeDeroxneBPtg/0?wx_fmt=jpeg'}, {'title': '农村改厕网上技术服务上线啦！', 'content_url': 'http://mp.weixin.qq.com/s?__biz=Mzg4NzA3OTQzMQ==&amp;mid=2247487613&amp;idx=1&amp;sn=71f02c21dbcc15d05baef9166d5d092a&amp;chksm=cf8e8715f8f90e03a955d82f8a64132e1620243ddf5748b10751a5e89acad46ed2b81c81480f&amp;scene=27#wechat_redirect', 'cover': 'http://mmbiz.qpic.cn/mmbiz_jpg/qEaZSLMQqa3kVtoical2plVIwToogU9FJzFzwLEQEc3icgNkJjQYvoATKC1OWnS9cFWt5VUFxhfCDiaXr5RdlEZfQ/0?wx_fmt=jpeg'}, {'title': '农业农村部召开以疫情防治为切入点 加强农村人居环境整治座谈会', 'content_url': 'http://mp.weixin.qq.com/s?__biz=Mzg4NzA3OTQzMQ==&amp;mid=2247487576&amp;idx=1&amp;sn=16f874e6ead29f6abe0b815febd88130&amp;chksm=cf8e8730f8f90e260c4b03734c9abe53568a5facfc2a40743359f008d59c3133433ec3d33fb4&amp;scene=27#wechat_redirect', 'cover': 'http://mmbiz.qpic.cn/mmbiz_jpg/qEaZSLMQqa3Lh3rRQWCRf2GPpFicCZic73MVKJ2InKlDwPweXKw9cw62xKQ7kmAfrcaSy5WZeGjaiaKIG4DP1XlZA/0?wx_fmt=jpeg'}
for d in lists:

    title = d['title']
    content_url = d['content_url']
    print(title,content_url)
    pdfkit.from_url(content_url, './pdf/' + title + '.pdf')
print("结束")



