#coding:utf-8
import requests
import json
import logging
import pytest
import allure


logging.basicConfig(level=logging.DEBUG)

def test_Api():
  log = logging.getLogger('test_Api')
  log.debug("this is warning message!!!")
  url = "https://m.qccr.com/api/userprod/user/queryGeeAuthCode?t=1588304436890&api=superapi&phone=17046689470&type=1"
  # logging.debug("创建链接URL" + url)
  # print("hello world!!!!!!!")
  payload = {}
  headers = {
    'Cookie': 'connect.sid=s%3AwsvvsN6WJLrhbOdRqzRN-PLJd2q37Kvi.owIjHZkOCPdGu4wbvChpKHSDiF0m6DW%2FwV5w%2B546bbY'
  }
  # logging.debug("创建header" + headers)

  response = requests.request("GET", url, headers=headers, data=payload)
  # logging.debug("发送请求，获取返回")
  jr = json.loads(response.text)
  # logging.debug("将返回的结果转换为json")
  msg = jr.get("msg")
  # logging.debug("获取返回中的msg")
  # code = jr.get("code")
  assert msg == "成功"

# if __name__ == '__main__':
#     pytest.main()
