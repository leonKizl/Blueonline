from requests import Response


class Checkig_status():
    @staticmethod
    def check_status_code(response:Response,status_code):
        assert response.status_code == status_code
        if response.status_code == status_code:
            print(f"Status code is correct - {status_code}")
        else:
            print(f"Status code is incorrect - {response.status_code}")
