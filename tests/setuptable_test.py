from time import sleep
import src.setuptable as setuptable
import pytest

success_msg = 'ok'
error_msg = 'fail' 
test_url = "http://localhost:8000/index"


def try_test():
    txt = success_msg
    return txt

def test_my_server():  #pragma: no cover

    def test_1():    
        assert try_test() == success_msg
   
    try:
        test_1()
        
    
    finally:
        print("ok!")
        
  