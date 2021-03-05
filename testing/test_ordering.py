from time import sleep

import pytest

@pytest.mark.run(order=10)
def test_1():
    sleep(1)
    assert True

"""pytest-ordering 插件：
通过装饰器 给指定测试用例设置执行顺序
不超过10 可以用 @pytest.mark.third 方式 直接通过数字英文
超过10 用order=2 方式来表达：@pytest.mark.run(order=2)
根据数字由小到大进行排序执行，如果不加order 则为最后一个执行

pytest-xdist插件：
分布式执行测试用例
terminal 上输入：pytest test_ordering.py -n 3
-n 3:创建三个线程分别执行一个测试用例
使用原则：用例之间是没有依赖关系，用例可以独立运行

"""
# @pytest.mark.third
def test_2():
    sleep(1)
    assert True

@pytest.mark.run(order=9)
def test_3():
    sleep(1)
    assert 1==1


