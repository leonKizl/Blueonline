import token

import requests

from Utilits.logger import Logger


class Http_method():

    cookie = ""

    @staticmethod
    def get(url,token):
        Logger.add_request(url, method="GET")
        result_get = requests.get(url, headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}, cookies = Http_method.cookie)
        Logger.add_response(result_get)
        return result_get

    @staticmethod
    def post(url, body, token):
        Logger.add_request(url, method="POST")
        result_post = requests.post(url, json = body, headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}, cookies = Http_method.cookie)
        Logger.add_response(result_post)
        return result_post

    @staticmethod
    def put(url, body, token):
        Logger.add_request(url, method="PUT")
        result_put = requests.put(url, json = body, headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}, cookies = Http_method.cookie)
        Logger.add_response(result_put)
        return result_put

    @staticmethod
    def delete(url, body, token):
        Logger.add_request(url, method="DELETE")
        result_delete = requests.delete(url, json = body, headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}, cookies = Http_method.cookie)
        Logger.add_response(result_delete)
        return result_delete