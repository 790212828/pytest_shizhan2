

import pytest

@pytest.fixture(params=[1,2,3])
def login1(request):
    print("test_params 下面的 login1")
    print(request.param)
    print("获取测试数据")
    data=request.param
    return data
    pass

def test_case1(login1):
    print("测试用例1")












