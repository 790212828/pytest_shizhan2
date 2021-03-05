import pytest


def test_a():
    print("test_demo.py test_a  打印提示")
def test_b():
    print("test_demo.py test_b  打印提示")
def test_c():
    print("test_demo.py test_c  打印提示")
    assert 2==1
@pytest.mark.parametrize('a',[1,2,3])
@pytest.mark.parametrize('b',[4,5,6])
def test_param(a,b):
    print(f"a={a},b={b}")










