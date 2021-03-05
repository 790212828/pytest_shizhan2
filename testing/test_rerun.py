import pytest
from time import sleep

"""
通过命令行执行 pytest test_rerun --reruns 3 --reruns-delay 1
--reruns 3 执行失败用例重跑三次
--reruns-delay 1 执行重跑间隔 1秒

通过装饰器去执行 ：
@pytest.mark.flaky(reruns=5,reruns_delay=2)
@pytest.mark.flaky(reruns=5,reruns_delay=3)

"""


def test_rerun1():
    sleep(0.5)
    assert 1==2


def test_rerun2():
    sleep(0.5)
    assert 2==2

@pytest.mark.flaky(reruns=5,reruns_delay=3)
def test_rerun3():
    sleep(0.5)
    assert 3==2










