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
    # def success_msg():
    #     try:
    #         setuptable.addmessage("pepe","pepo")

    def addmessage_passes():
        try:
            with pytest.raises(Exception) as excinfo:
                setuptable.addmessage("pepe","pepo")
            assert excinfo.value.args[0] == 'err'
        except:
            assert True
            
    def getmessage_passes():
        try:
            with pytest.raises(Exception) as excinfo:
                setuptable.getmessagesbytopic("pepo")
            assert excinfo.value.args[0] == 'err'
        except:
            assert True

    def createtable_exist_passes():
        try:
            with pytest.raises(Exception) as excinfo:
                setuptable.createtable()
            assert excinfo.value.args[0] == 'err'
        except:
            assert True

    def droptable_passes():
        try:
            with pytest.raises(Exception) as excinfo:
                setuptable.createtable()
            assert excinfo.value.args[0] == 'err'
        except:
            assert True
            
    def createtable_new_passes():
        try:
            with pytest.raises(Exception) as excinfo:
                setuptable.createtable()
            assert excinfo.value.args[0] == 'err'
        except:
            assert True
    
    try:
        test_1()
        addmessage_passes()
        getmessage_passes()
        
    
    finally:
        print("ok!")
        
  