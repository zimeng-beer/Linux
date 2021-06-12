# coding ：UTF-8
# 开发团队：  XX科技
# 开发人员： 
# 开发时间： 2021/5/22   16:06
# 文件名称： test_test.py
# 开发工具： PyCharm
#
# list = [ { 'a':'1' , 'b':'2' , 'c':'3' }, { 'd':'4' , 'e':'5' , 'f':'文字' } ]
# #list = [ { 'a':1 , 'b':2 , 'c':3 }, { 'd':4 , 'e':5 , 'f':6 } ]
#
# for sub in list:
#     for f in sub:
#         sub[f]=int(sub[f])
# print(list)


import requests
url="https://piao.qunar.com//ticket/list.htm?keyword=上海&amp;region=上海&amp;from=mpshouye_hotcity"
rep=requests.get(url=url)
print(rep.text)