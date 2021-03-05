import allure
import pytest
import yaml

from python_code.calc import Calculator

with open("./datas/calc.yaml") as f:
    datas=yaml.safe_load(f)['add']
    add_datas=datas['datas_true']
    print(add_datas)
    myid=datas['myid_true']
    print(myid)

@pytest.fixture(params=add_datas,ids=myid)
def get_datas(request):
    print("开始计算")
    data=request.param
    print(f"测试数据为：{data}")
    yield data
    print("计算结束")

@allure.feature("测试计算器")
class TestCalc:
    # def setup_class(self):
    #     # 实例化计算器的类
    #     print("开始计算，实例化计算类")
    #     self.calc=Calculator()
    # def teardown_class(self):
    #     print("计算结束！！！")

    """
    优化点：
    1、把 setup、teardown 方法换成了fixture方法的 get_calc
    2、把 get_calc 方法放到 conftest中
    3、把 参数化 parametrize 换为了 fixture 参数化方式
    4、测试用例中的数据需要通过 get_datas方法获取到列表数据
    get_datas 返回列表[1,1,2] 需要测试用例里面 调用 列表的索引值 去赋值变量，分别代表了a,b,expect

    """
    @allure.story("测试加法")
    @pytest.mark.add
    def test_add(self,get_calc,get_datas):
        """
        实例化计算器的类
        :return:
        """
        # calc=Calculator()
        # 调用add方法
        with allure.step("计算两个数的相加和"):
            result=get_calc.add(get_datas[0],get_datas[1])
        # 判断result 是否是浮点数，做出保留小数点后2位的处理
        with allure.step("判断result 是否是浮点数"):
            if isinstance(result,float):
                result=round(result,2)#避免浮点数计算 python底层转换二进制进行计算的错误，需要round函数进行四舍五入
        # 得到结果之后，需要写断言
        with allure.step("断言计算结果和预期结果"):
            assert result==get_datas[2]