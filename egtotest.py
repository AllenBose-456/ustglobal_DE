import pytest
def case(x):
    if not isinstance(x,str):
        raise TypeError("enter string as an arguement")
    return x.capitalize()

def test_case():
    assert case('semaphore')=='Semaphore'

def test_raises_exception_on_non_string():
    with pytest.raises(TypeError):
        case(9)