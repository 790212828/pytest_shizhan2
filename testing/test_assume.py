
"""
pytest-assume:
是一个执行全部用例的代码
告诉所有出错的地方
==报错继续运行代码的功能插件
"""
import pytest


def test_a():
    # assert 1==2
    # assert False==True
    # assert 100==200
    pytest.assume(1==1)
    pytest.assume(False==True)
    pytest.assume(100==200)
    pytest.assume(1==2)






