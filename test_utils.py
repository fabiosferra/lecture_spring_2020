from utils import funny

def test_funny():
    assert funny(2, 1) == 3

def test_funny_2():
    assert funny(2, 'a') == 3
