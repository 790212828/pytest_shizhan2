import pytest

#fixture 的优先级比setup 高
def setup():
    print("执行setup")


# 用pytest.fixture标记测试用例需要执行的前提方法
#autouse=True,作用域里面所有测试用例都调用fixture
# @pytest.fixture(autouse=True)
@pytest.fixture()
def login():
    print("登陆操作")
    print("获取token")
    username="test_name"
    password="123456"
    token="token136u43432jdu23"

    #yield 关键字可以激活fixture 的teardown功能，
    #也就是说启用了yield 关键字后 后面代码都是执行teardown操作
    yield [username,password,token]
    print("注销操作")


# 测试用例1：需要提前登陆
#在测试用例中传入 fixture 标记的方法名称
def test_case1(login):
    #获取fixture方法里的返回值，直接调用fixture方法名称
    #yield 相当于return，返回数据可以直接跟在yield后面
    print(f"用户信息为：{login}")
    print("测试用例1")


def test_case2(connectDB):
    print("测试用例2")
#测试用例3：需要提前登陆
def test_case3(login):
    print("测试用例3")
#测试用例3：需要提前登陆,
# 使用pytest装饰器方法传入，需要传入执行的方法名称 string类型
@pytest.mark.usefixtures("login")
def test_case4():
    print("测试用例4")


