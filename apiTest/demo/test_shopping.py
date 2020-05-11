# coding=utf-8
import pytest
import allure
import requests
import json

@allure.feature("发送短信功能")
class TestSentMsg(object):
    @allure.story("拼装链接并发送请求")
    def test_send_msg(self):
        url = "https://m.qccr.com/api/userprod/user/queryGeeAuthCode?t=1588304436890&api=superapi&phone=17046689470&type=1"
        payload = {}
        headers = {
            'Cookie': 'connect.sid=s%3AwsvvsN6WJLrhbOdRqzRN-PLJd2q37Kvi.owIjHZkOCPdGu4wbvChpKHSDiF0m6DW%2FwV5w%2B546bbY'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        jr = json.loads(response.text)
        msg = jr.get("msg")
        assert msg == "失败"
