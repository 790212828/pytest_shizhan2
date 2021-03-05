import pytest


# @pytest.fixture(scope="function")
# @pytest.fixture(scope="class")
# @pytest.fixture(scope="module")
# def connectDB():
#     print("\n连接数据库操作")
#     yield
#     print("断开数据库连接")


class  TestDemo:
    def test_a(self,connectDB):
        print("测试用例a")

    def test_b(self,connectDB):
        print("测试用例b")
class  TestDemo2:
    def test_c(self,connectDB):
        print("测试用例c")

    def test_d(self,connectDB):
        print("测试用例d")




