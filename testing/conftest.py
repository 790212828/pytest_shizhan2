import yaml

import pytest



# @pytest.fixture(scope="function")
# @pytest.fixture(scope="class")
# @pytest.fixture(scope="module")
from python_code.calc import Calculator


@pytest.fixture(scope="session")
def connectDB():
    print("\n连接数据库操作")
    yield
    print("断开数据库连接")

@pytest.fixture(scope="module")
def get_calc():
    print("实例化计算器类")
    calc=Calculator()
    print("fixture方法 开始计算")
    yield calc
    print("fixture方法 计算结束")

with open("./datas/calc2.yaml") as f:
    datas = yaml.safe_load(f)
    #获取 add、sub、mul、div 下的数据
    datas_add=datas["add"]
    datas_div = datas["div"]
    datas_sub=datas["sub"]
    datas_mul=datas["mul"]
    #获取加法下的 datas_True 、datas_False 数据
    add_datas_True = datas_add["datas_True"]
    add_datas_False = datas_add["datas_False"]
    # 获取除法下的 datas_True 、datas_False 数据
    div_datas_True = datas_div["datas_True"]
    div_datas_False = datas_div["datas_False"]
    # 获取减法下的 datas_True 、datas_False 数据
    sub_datas_True=datas_sub["datas_True"]
    sub_datas_False=datas_sub["datas_False"]
    # 获取乘法下的 datas_True 、datas_False 数据
    mul_datas_True=datas_mul["datas_True"]
    mul_datas_False=datas_mul["datas_False"]




#加法测试用例数据参数化
@pytest.fixture(params=add_datas_True)
def get_add_datas_True(request):
    print("返回-加法正常用例 参数化 数据")
    data=request.param
    yield data
    print("加法正常用例-返回结束 下一条 参数")

@pytest.fixture(params=add_datas_False)
def get_add_datas_False(request):
    print("返回-加法异常用例 参数化 数据")
    data=request.param
    yield data
    print("加法异常用例-返回结束 下一条 参数")
#除法测试用例数据参数化
@pytest.fixture(params=div_datas_True)
def get_div_datas_True(request):
    print("返回-除法正常用例 参数化 数据")
    data=request.param
    yield data
    print("除法正常用例-返回结束 下一条 参数")

@pytest.fixture(params=div_datas_False)
def get_div_datas_False(request):
    print("返回-除法异常用例 参数化 数据")
    data=request.param
    yield data
    print("除法异常用例-返回结束 下一条 参数")

#减法测试用例数据参数化
@pytest.fixture(params=sub_datas_True)
def get_sub_datas_True(request):
    print("返回-减法正常用例 参数化 数据")
    data=request.param
    yield data
    print("减法正常用例-返回结束 下一条 参数")

@pytest.fixture(params=sub_datas_False)
def get_sub_datas_False(request):
    print("返回-减法异常用例 参数化 数据")
    data=request.param
    yield data
    print("减法异常用例-返回结束 下一条 参数")

#乘法测试用例数据参数化
@pytest.fixture(params=mul_datas_True)
def get_mul_datas_True(request):
    print("返回-乘法正常用例 参数化 数据")
    data=request.param
    yield data
    print("减法正常用例-返回结束 下一条 参数")
@pytest.fixture(params=mul_datas_False)
def get_mul_datas_False(request):
    print("返回-乘法异常用例 参数化 数据")
    data=request.param
    yield data
    print("乘法异常用例-返回结束 下一条 参数")
