本目录下是用来做接口测试的目录，以下是本项目中做接口测试的一些规范
1、每个接口在执行测试之前需要定义三个参数，分别为url,pauload,header,其中url为空，payload和headers为空json
2、返回的参数中要将返回的cookie，header,response同时返回
3、第一阶段的断言规范中要使用pytest做断言，由于业务的不同，大家可以根据各自业务的特点来定，本项目暂时以返回的状态码和返回的msg作为我们的断言标准
4、使用本项目时需要安装pytest

import requests
url = ""
payload = {}
headers= {}
response = requests.request("GET", url, headers=headers, data = payload)
print(response.text.encode('utf8'))
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
brew install allure
py.test  --alluredir ./result/
allure generate ./result/ -o ./report/ --clean
https://brew.sh/index_zh-cn
https://www.kancloud.cn/qadoc/allure/841196
