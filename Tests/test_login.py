from Utilits import Checking
from Utilits.login import Login
from Utilits.Checking import Checkig_status


class Test_login():

    def test_login(self):
        print("Correct login")
        result_post = Login.login_correct()
        Checkig_status.check_status_code(result_post, 200)

        print("Incorrect login")

        result_post = Login.login_incorrect()
        Checkig_status.check_status_code(result_post, 403)

        print("Incorrect login 2")

        result_post = Login.login_incorrect_2()
        Checkig_status.check_status_code(result_post,422)

