import pytest

from main_program import *
def test_answer():
    assert add(3,6,)==9

def test_answer2():

    with pytest.raises(ZeroDivisionError):
      assert divide(3,0,)==2

