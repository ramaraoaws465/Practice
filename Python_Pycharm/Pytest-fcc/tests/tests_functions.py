import time

import pytest
import source.my_functions as my_functions


#from string_methods import result

def test_add():
    result = my_functions.add(1, 6)
    assert result == 7

def test_add_strings():
    result =  my_functions.add("i like", " burgers")
    assert result == "i like burgers"

def test_divide():
    result = my_functions.divide(10, 5)
    assert result == 2
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
     my_functions.divide(10, 1)
    #assert True

@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(10, 5)
    assert result == 2