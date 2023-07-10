import requests
import datetime
from config import start_time
from config import referer
from config import Cookie
from config import stdid
from config import bianhao as stateID
start_time = str(start_time)
#获取当前日期
end_time = datetime.datetime.now().strftime('%Y-%m-%d')
#计算日期差天数
days = (datetime.datetime.strptime(start_time, '%Y-%m-%d') - datetime.datetime.strptime(end_time, '%Y-%m-%d')).days + 2
#每天差十九个数，起始数为stateID
stateID = int(stateID)
final_stateID = stateID + days * 19
url = 'http://yycdjxx.gsjiapei.com/Server/OrderCoachServer.asmx/orderCoachNew?_=' + stdid
payload = {'PXResID': "", 'SubID': "2", 'stateID': ""}
#playload的第三个参数为字符串类型的final_stateID
payload['stateID'] = str(final_stateID)
headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '45',
    'Content-Type': 'application/json; charset=UTF-8',
    'Cookie': 'ASP.NET_SessionId=' + Cookie,
    'Host': 'yycdjxx.gsjiapei.com',
    'Origin': 'http://yycdjxx.gsjiapei.com',
    'Referer': 'http://yycdjxx.gsjiapei.com/NMobile/page/timenew.html?ts=' + referer,
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
