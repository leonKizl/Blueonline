import requests

from Utilits import http_method
from Utilits.http_method import Http_method

base_url = "https://api.dev.demo.blueonline.tv"


class Parental_control():


    @staticmethod
    def subscriber_details(token):
        url_path = "/subscriber/details?platform=BROWSER&system=tvonline&language=pl"
        url_get_subscriber_details = base_url + url_path
        result_get = Http_method.get(url_get_subscriber_details,token)
        print("\nGET request to subscriber/details")
        return result_get

    @staticmethod
    def parents_control_enable(token,rating):
        url_path = "/subscriber/parental/enable?platform=BROWSER&system=tvonline"
        url_post_18 = base_url + url_path
        json_for_post = {
            "rating": rating
        }
        result_post = Http_method.post(url_post_18, json_for_post, token)
        print("POST request to enable parental control")
        print(result_post.text)
        return result_post


    @staticmethod
    def parents_control_disable(token):
        url_path = "/subscriber/parental/disable?platform=BROWSER&system=tvonline"
        url_disable = base_url + url_path
        json_for_post = {"pin": "1234"}
        result_post = Http_method.post(url_disable, json_for_post, token)
        print("POST request to disable parental control")
        print(result_post.text)
        return result_post
    @staticmethod
    def add_to_favourites(token,uuid):
        print("POST request to add products with different ratings to favourites")

        url_path = "/subscriber/bookmarks/favourite/create?platform=BROWSER&system=tvonline"
        url_favourite = base_url + url_path


        json_for_post = { "productUuid":uuid,"type":"channel"}

        result_post = Http_method.post(url_favourite, json_for_post, token)
        return result_post

    @staticmethod
    def get_all_favourites_products(token):
        print("Get all favourites products")
        url_path = "/subscriber/bookmarks/favourite?platform=BROWSER&system=tvonline&language=pl"
        url_get = base_url + url_path
        result_get = Http_method.get(url_get, token)
        return result_get

    @staticmethod
    def get_products_details(uuid,token):
        url_path = f"{base_url}/products/vod/{uuid}?platform=BROWSER&system=tvonline&language=pl"
        result_get = Http_method.get(url_path,token)
        print("\n-----\n-----\n")
        print(url_path)
        print(result_get.text)
        return result_get

    @staticmethod
    def get_products_details_with_rating(uuid,token,rating):
        url_path = f"{base_url}/products/vod/{uuid}?platform=BROWSER&system=tvonline&rating={rating}&language=pl"
        print(f"Open products details with parental control ({rating})\n get request to {url_path}")
        result_get = Http_method.get(url_path,token)
        metadata = (result_get.json()).get("metadata")
        rat = (result_get.json()).get('rating')
        print(metadata)
        print(rat)
        return result_get
