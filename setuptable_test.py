from time import sleep
import pytest
import setuptable


success_msg = 'Success: Login Sucessful.'
error_msg = 'Error: Invalid Credentials. Please try again.' 
test_url = "http://localhost:8000/index"


def try_login():
    txt = success_msg
    return txt

def test_my_server():  #pragma: no cover

    def test_login_correct_user_and_password():    
        assert try_login() == success_msg

    
    try:
        test_login_correct_user_and_password()
    
    finally:
        print("ok!")
        
  