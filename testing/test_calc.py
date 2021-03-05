import pytest
import yaml
from python_code.calc import Calculator



with open("./datas/calc.yaml") as f:
    datas=yaml.safe_load(f)['add']
    add_datas=datas['datas_true']
    print(add_datas)
    myid=datas['myid_true']
    print(myid)
def test_a():
    print("测试用例a")

def func():
    print("普通函数")

class TestCalc:
    def setup_class(self):
        # 实例化计算器的类
        print("开始计算，实例化计算类")
        self.calc=Calculator()
    def teardown_class(self):
        print("计算结束！！！")


    @pytest.mark.parametrize(
        "a,b,expect",
        # [
        #     (1,1,2),
        #     (0.1,0.1,0.2),
        #     (-1,-1,-2),
        #     (0.1,0.2,0.3)
        # ]
        # add_datas,ids=['int','float','negative','round']#给列表里的三个用例起名字
        # add_datas,ids=['int','float','round','fail','negative']
        add_datas,ids=myid
    )
    def test_add(self,a,b,expect):
        """
        实例化计算器的类
        :return:
        """
        # calc=Calculator()
        # 调用add方法
        result=self.calc.add(a,b)
        # 判断result 是否是浮点数，做出保留小数点后2位的处理
        if isinstance(result,float):
            result=round(result,2)#避免浮点数计算 python底层转换二进制进行计算的错误，需要round函数进行四舍五入
        # 得到结果之后，需要写断言
        assert result==expect

    @pytest.mark.add()
    def test_add3(self):
        result=self.calc.add(0.1,0.2)
        #判断result 是否是浮点数，做出保留小数点后2位的处理
        if isinstance(result,float):
            result=round(result,2)
        assert result==0.3#避免浮点数计算 python底层转换二进制进行计算的错误，需要round函数进行四舍五入

    def test_add1(self):
        """
        实例化计算器的类
        :return:
        """
        # calc=Calculator()
        # 调用add方法
        result=self.calc.add(0.1,0.1)
        # 得到结果之后，需要写断言
        assert result==0.2
    def test_add2(self):
        """
        实例化计算器的类
        :return:
        """
        # calc=Calculator()
        # 调用add方法
        result=self.calc.add(-1,-1)
        # 得到结果之后，需要写断言
        assert result==-2

    @pytest.mark.sub
    def test_sub(self):
        print("test_sub")

    @pytest.mark.div
    def test_div(self):
        print("test_div")

    @pytest.mark.mul
    def test_mul(self):
        print("test_mul")






