import allure
import requests
import json
import pytest

@allure.feature("测试成功用例")
def test_Api():
  url = "https://m.qccr.com/api/userprod/user/queryGeeAuthCode?t=1588304436890&api=superapi&phone=17046689470&type=1"

  payload = {}
  headers = {
    'Cookie': 'connect.sid=s%3AwsvvsN6WJLrhbOdRqzRN-PLJd2q37Kvi.owIjHZkOCPdGu4wbvChpKHSDiF0m6DW%2FwV5w%2B546bbY'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  jr = json.loads(response.text)
  msg = jr.get("msg")
  # code = jr.get("code")
  assert msg == "成功"

if __name__ == '__main__':
    pytest.main()
