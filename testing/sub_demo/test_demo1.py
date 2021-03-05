import pytest


@pytest.fixture()
def connectDB():
    print("test_demo1 下面的 connectDB 连接数据库操作")
    yield
    print("test_demo1 下面的 disconnectDB 断开数据库连接操作")



def test_a(connectDB):
    print("sub_demo test_a")

class TestA:
    def test_b(self):
        print("sub_demo test_b")


