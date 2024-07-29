import json

import requests

from Utilits.add_to_favourite import Parental_control
from Utilits.Checking import Checkig_status


class Test_to_add():
    def test_subscriber_details(self):
        # SEND REQUEST TO RECIEVE TOKEN:
        headers_for_login = {
            "Content-Type": "application/json",
            "API-Device": "Chrome; 125; Mac OS; 10.15.7; Mac OS; 10.15.7;"
        }
        data = {"os": "Mac OS", "osVersion": "10.15.7", "maker": "unknown", "agent": "Chrome",
                "login": "leonid-955@mail.ru", "password": "Testowanie99",
                "uid": "529c4239-0f1a-4df9-bcd8-a4bf8d556b85"}
        url_for_log = "https://api.dev.demo.blueonline.tv/subscriber/login?platform=BROWSER&system=tvonline"
        Login_in_system = requests.post(url_for_log, json=data, headers=headers_for_login)
        result_from_loging = Login_in_system.json()
        token = result_from_loging.get("token")
        # 1. With token after signin in get info about subscriber

        result_get = Parental_control.subscriber_details(token)
        rating = (result_get.json()).get("parental_control_rating")
        print(f"User with parental control - {rating}")
        Checkig_status.check_status_code(result_get,200)

        print(f"\n-----\n")
        #
        # 2. Check if there are any favourites products
        result_get = Parental_control.get_all_favourites_products(token)

        response_data = json.loads(result_get.text)
        print(f"Number of products: {len(response_data)}")
        # Print the UUIDs of the products
        print("Product UUIDs:")
        for product in response_data:
            print(product.get('uuid'))

        Checkig_status.check_status_code(result_get,200)

        # 3. Add movies with Rating 18
        uuid_18 = "4423d22a-e2fd-4335-8fd5-4aae60249768"
        # 16
        uuid_16 = "dcd29cb3-0cc6-44be-abcf-60dc57656211"
        # 12
        uuid_12 = "abd3660e-e993-4463-9d5e-9230080502d0"
        # 7
        uuid_7 = "1de4d099-f156-4321-aec3-a76169a7b630"
        # 0
        uuid_0 = "cce3e4bb-82fc-4324-8e46-97de41419028"

        result_post = Parental_control.add_to_favourites(token,uuid_18)
        print(result_post.text)
        uuid = (result_post.json()).get("product_uuid")
        print(uuid)
        Checkig_status.check_status_code(result_post,200)


        # 4. Enable parental control (18)

        result_post = Parental_control.parents_control_enable(token,18)
        token = (result_post.json()).get("token")
        rating = (result_post.json()).get("rating")
        Checkig_status.check_status_code(result_post,200)

        # 5. Try to open product/details with PC rating 18
        # # With new token from response disable parental control
        print(f"\n---\n---\nWith PC 18 get info about product with rating 18")

        result_get = Parental_control.get_products_details_with_rating(uuid_18,token,rating)
        Checkig_status.check_status_code(result_get,200)

        print(f"With PC {rating} get info about product with rating 16")

        result_get = Parental_control.get_products_details_with_rating(uuid_16, token, rating)
        Checkig_status.check_status_code(result_get, 200)

        print(f"With PC {rating} get info about product with rating 12")

        result_get = Parental_control.get_products_details_with_rating(uuid_12, token, rating)
        Checkig_status.check_status_code(result_get, 200)

        print(f"With PC {rating} get info about product with rating 7")

        result_get = Parental_control.get_products_details_with_rating(uuid_7, token, rating)
        Checkig_status.check_status_code(result_get, 200)

        print(f"With PC {rating} get info about product with rating 0")

        result_get = Parental_control.get_products_details_with_rating(uuid_0, token, rating)
        Checkig_status.check_status_code(result_get, 200)



        # 6. Disable parental control and enable parental for rating 16


        result_post = Parental_control.parents_control_disable(token)
        token = (result_post.json()).get("token")
        Checkig_status.check_status_code(result_post,200)
        print(f"\n-----\n")

        result_post = Parental_control.parents_control_enable(token,16)
        token = (result_post.json()).get("token")
        rating = (result_post.json()).get("rating")

        # 7. Try to get info about product, whith PC 16
        print(f"With PC {rating} get info about product with rating 18")
        result_get = Parental_control.get_products_details_with_rating(uuid_18,token,rating)
        Checkig_status.check_status_code(result_get,400)

        print(f"With PC {rating} get info about product with rating 16")

        result_get = Parental_control.get_products_details_with_rating(uuid_16, token, rating)
        Checkig_status.check_status_code(result_get, 200)

        print(f"With PC {rating} get info about product with rating 12")

        result_get = Parental_control.get_products_details_with_rating(uuid_12, token, rating)
        Checkig_status.check_status_code(result_get, 200)

        print(f"With PC {rating} get info about product with rating 7")

        result_get = Parental_control.get_products_details_with_rating(uuid_7, token, rating)
        Checkig_status.check_status_code(result_get, 200)

        print(f"With PC {rating} get info about product with rating 0")

        result_get = Parental_control.get_products_details_with_rating(uuid_0, token, rating)
        Checkig_status.check_status_code(result_get, 200)


        # 8. Disable parental control and enable parental for rating 12
        result_post = Parental_control.parents_control_disable(token)
        token = (result_post.json()).get("token")
        Checkig_status.check_status_code(result_post,200)

        result_post = Parental_control.parents_control_enable(token, 12)
        token = (result_post.json()).get("token")
        rating = (result_post.json()).get("rating")

#       # 9. Try to get info about product, which is not allowing coz of parental
        print(f"With PC {rating} get info about product with rating 18")
        result_get = Parental_control.get_products_details_with_rating(uuid_18,token,rating)
        Checkig_status.check_status_code(result_get,400)

        print(f"With PC {rating} get info about product with rating 16")

        result_get = Parental_control.get_products_details_with_rating(uuid_16, token, rating)
        Checkig_status.check_status_code(result_get, 400)

        print(f"With PC {rating} get info about product with rating 12")

        result_get = Parental_control.get_products_details_with_rating(uuid_12, token, rating)
        Checkig_status.check_status_code(result_get, 200)

        print(f"With PC {rating} get info about product with rating 7")

        result_get = Parental_control.get_products_details_with_rating(uuid_7, token, rating)
        Checkig_status.check_status_code(result_get, 200)

        print(f"With PC {rating} get info about product with rating 0")

        result_get = Parental_control.get_products_details_with_rating(uuid_0, token, rating)
        Checkig_status.check_status_code(result_get, 200)

        # 10. Disable parental control and enable parental for rating 7
        result_post = Parental_control.parents_control_disable(token)
        token = (result_post.json()).get("token")
        Checkig_status.check_status_code(result_post, 200)

        result_post = Parental_control.parents_control_enable(token, 7)
        token = (result_post.json()).get("token")
        rating = (result_post.json()).get("rating")

        # 11. Try to get info about product, which is not allowing coz of parental
        print(f"With PC {rating} get info about product with rating 18")
        result_get = Parental_control.get_products_details_with_rating(uuid_18, token, rating)
        Checkig_status.check_status_code(result_get, 400)

        print(f"With PC {rating} get info about product with rating 16")

        result_get = Parental_control.get_products_details_with_rating(uuid_16, token, rating)
        Checkig_status.check_status_code(result_get, 400)

        print(f"With PC {rating} get info about product with rating 12")

        result_get = Parental_control.get_products_details_with_rating(uuid_12, token, rating)
        Checkig_status.check_status_code(result_get, 400)

        print(f"With PC {rating} get info about product with rating 7")

        result_get = Parental_control.get_products_details_with_rating(uuid_7, token, rating)
        Checkig_status.check_status_code(result_get, 200)

        print(f"With PC {rating} get info about product with rating 0")

        result_get = Parental_control.get_products_details_with_rating(uuid_0, token, rating)
        Checkig_status.check_status_code(result_get, 200)

        # 12. Disable parental control and enable parental for rating 0
        result_post = Parental_control.parents_control_disable(token)
        token = (result_post.json()).get("token")
        Checkig_status.check_status_code(result_post, 200)

        result_post = Parental_control.parents_control_enable(token, 0)
        token = (result_post.json()).get("token")
        rating = (result_post.json()).get("rating")

        # 13. Try to get info about product, which is not allowing coz of parental
        print(f"With PC {rating} get info about product with rating 18")
        result_get = Parental_control.get_products_details_with_rating(uuid_18, token, rating)
        Checkig_status.check_status_code(result_get, 400)

        print(f"With PC {rating} get info about product with rating 16")

        result_get = Parental_control.get_products_details_with_rating(uuid_16, token, rating)
        Checkig_status.check_status_code(result_get, 400)

        print(f"With PC {rating} get info about product with rating 12")

        result_get = Parental_control.get_products_details_with_rating(uuid_12, token, rating)
        Checkig_status.check_status_code(result_get, 400)

        print(f"With PC {rating} get info about product with rating 7")

        result_get = Parental_control.get_products_details_with_rating(uuid_7, token, rating)
        Checkig_status.check_status_code(result_get, 400)

        print(f"With PC {rating} get info about product with rating 0")

        result_get = Parental_control.get_products_details_with_rating(uuid_0, token, rating)
        Checkig_status.check_status_code(result_get, 200)

        # 14. Disable parental
        result_post = Parental_control.parents_control_disable(token)
        token = (result_post.json()).get("token")
        rating = (result_post.json()).get("rating")

        result_get = Parental_control.get_products_details(uuid_18, token)
        Checkig_status.check_status_code(result_get, 200)

        uunid = "80993682-73a7-4969-909f-94a089959571"
        print("TEST")
        result_get = Parental_control.get_products_details(uunid,token)







