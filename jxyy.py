import requests
import datetime
from config import referer
from config import userName
from config import pwd
from config import stdid
from config import bianhao as stateID
from config import start_time
import requests
from bs4 import BeautifulSoup

# 构造登录请求的URL和数据
url = "http://glcdjx.gsjiapei.com/UserHome/StuBind"
data = {
    "userName": userName,
    "pwd": pwd
}

# 构造会话对象，保持cookie
session = requests.session()

# 发送GET请求，获取登录页面的HTML代码
response = session.get(url)

# 解析HTML代码，找到账号和密码的input标签，并填入账号密码
soup = BeautifulSoup(response.text, "html.parser")
username_input = soup.find("input", {"id": "userName"})
password_input = soup.find("input", {"id": "pwd"})
username_input["value"] = data["userName"]
password_input["value"] = data["pwd"]

# 模拟点击登录按钮，发送POST请求，获取登录后的cookie
login_button = soup.find("input", {"id": "btnLogin"})
response = session.post(url, data=data)

# 获取登录后的cookie
cookie = session.cookies.get_dict()
print(cookie)

#获取该cookie下的ASP.NET_SessionId的值
Cookie = cookie['ASP.NET_SessionId']

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
