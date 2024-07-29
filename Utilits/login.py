import requests

from Utilits.http_method import Http_method

url = "https://api.dev.demo.blueonline.tv/subscriber/login?platform=BROWSER&system=tvonline"
headers_for_login = {
            "Content-Type": "application/json",
            "API-Device": "Chrome; 125; Mac OS; 10.15.7; Mac OS; 10.15.7;"  # Замените на правильное значение
        }
class Login():
    @staticmethod
    def login_correct():
        body = {
            "os": "Mac OS", "osVersion": "10.15.7", "maker": "unknown", "agent": "Chrome",
            "login": "leonid-955@mail.ru", "password": "Testowanie99",
            "uid": "529c4239-0f1a-4df9-bcd8-a4bf8d556b85"
        }
        result_post = requests.post(url,json=body,headers=headers_for_login)

        msg = (result_post.json()).get("message")
        print(msg)
        return result_post

    @staticmethod
    def login_incorrect():
        body = {
            "os": "Mac OS", "osVersion": "10.15.7", "maker": "unknown", "agent": "Chrome",
            "login": "leonid-955@mail.ru", "password": "99",
            "uid": "529c4239-0f1a-4df9-bcd8-a4bf8d556b85"
        }
        result_post = requests.post(url, json=body, headers=headers_for_login)
        msg = (result_post.json()).get("message")
        print(msg)
        return result_post

    @staticmethod
    def login_incorrect_2():
        body = {
            "os": "Mac OS", "osVersion": "10.15.7", "maker": "unknown", "agent": "Chrome",
            "login": "leonid-955@mail.ru",
            "uid": "529c4239-0f1a-4df9-bcd8-a4bf8d556b85"
        }
        result_post = requests.post(url, json=body, headers=headers_for_login)
        msg = (result_post.json()).get("message")
        print(msg)
        return result_post
