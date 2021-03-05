
import pytest

@pytest.fixture()
def connectDB():
    print("sub_demo 下面的 connectDB 连接数据库操作")
    yield
    print("sub_demo 下面的 disconnectDB 断开数据库连接操作")







