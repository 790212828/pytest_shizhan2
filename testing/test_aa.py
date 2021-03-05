"""
课后作业
补全计算器中加法和除法的测试用例
使用参数化完成测试用例的自动生成
在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】

注意：
使用等价类，边界值，因果图等设计测试用例
测试用例中添加断言，验证结果
灵活使用 setup(), teardown() , setup_class(), teardown_class()

增加限制条件：
计算后输出长度限制：10**(-8) 到10**8
计算后输出 保留小数点后2位的处理


正常：
    0+0
    0+1
    0+(-1)
    int
输出边界值：len()<=9
    99999999+1
    (-99999999)+(-1)
    float
    99999999.9+0.1
    99999999.9+0.1


输出边界值：len()<=9
    int
    999999999+1
    (-999999999)+(-1)


https://wenku.baidu.com/view/370026aad1f34693daef3eeb.html
https://www.cnblogs.com/fnng/p/4774676.html

"""
import allure
import pytest
import yaml


from python_code.calc import Calculator




@allure.feature("测试计算器:(加减乘除)")
class TestCalc2:
    #加法测试用例
    # @pytest.mark.parametrize('a,b,expect',add_datas_True)
    @allure.story("测试加法_有效测试用例")
    @pytest.mark.add
    @pytest.mark.run(order=1)
    def test_add_True(self,get_calc,get_add_datas_True):
        with allure.step("计算两个数相加和"):
            result=get_calc.add(get_add_datas_True[0],get_add_datas_True[1])
        with allure.step("判断 相加和的数 是否为 float类型 "):
            if isinstance(result,float):
                with allure.step("相加和的数 为float类型，result 保留小数点后两位"):
                    result=round(result,2)
        with allure.step("断言 计算结果 等于 预期结果"):
            assert result==get_add_datas_True[2]


    # @pytest.mark.parametrize('a,b,expect',add_datas_False)
    @allure.story("测试加法_无效测试用例")
    @pytest.mark.add
    @pytest.mark.run(order=1)
    def test_add_Fasle(self,get_calc,get_add_datas_False):
        with allure.step("计算两个数相加和"):
            result = get_calc.add(get_add_datas_False[0], get_add_datas_False[1])
        with allure.step("判断 相加和的数 是否为 float类型 "):
            if isinstance(result,float):
                with allure.step("相加和的数 为float类型，result 保留小数点后两位"):
                    result = round(result,2)
        with allure.step("断言 计算结果 不等于 预期结果"):
            assert result != get_add_datas_False[2]

    # 除法测试用例
    # @pytest.mark.parametrize('a,b,expect', div_datas_True)
    @allure.story("测试除法_有效测试用例")
    @pytest.mark.div
    @pytest.mark.run(order=4)
    def test_div_True(self,get_calc,get_div_datas_True):
        with allure.step("判断 除数 是否为0"):
            if get_div_datas_True[1]==0:
                with allure.step("除数为0，用例执行失败"):
                    print("除数不能为0")
                    assert False
            else:
                with allure.step("除数不为0,计算 相除商的数值"):
                    result = get_calc.div(get_div_datas_True[0],get_div_datas_True[1])
                with allure.step("判断 相除商的数 是否为 float类型 "):
                    if isinstance(result, float):
                        with allure.step("相除商的数 为float类型，result 保留小数点后两位"):
                            result = round(result,2)
                with allure.step("断言 计算结果 等于 预期结果 "):
                    assert result == get_div_datas_True[2]

    # @pytest.mark.parametrize('a,b,expect', div_datas_False)
    @allure.story("测试除法_无效测试用例")
    @pytest.mark.div
    @pytest.mark.run(order=4)
    def test_div_False(self,get_calc,get_div_datas_False):
        with allure.step("判断 除数 是否为0"):
            if get_div_datas_False[1]==0:
                with allure.step("除数为0，用例执行失败"):
                    print("除数不能为0")
                    assert False
            else:
                with allure.step("除数不为0,计算 相除商的数值"):
                    result = get_calc.div(get_div_datas_False[0],get_div_datas_False[1])
                with allure.step("判断 相除商的数 是否为 float类型 "):
                    if isinstance(result, float):
                        with allure.step("相除商的数 为float类型，result 保留小数点后两位"):
                            result = round(result,2)
                with allure.step("断言 计算结果 不等于 预期结果 "):
                    assert result != get_div_datas_False[2]

    # 减法测试用例
    @allure.story("测试减法_有效测试用例")
    @pytest.mark.sub
    @pytest.mark.run(order=2)
    def test_sub_True(self,get_calc,get_sub_datas_True):
        with allure.step("计算两个数 相减差结果"):
            result=get_calc.sub(get_sub_datas_True[0],get_sub_datas_True[1])
        with allure.step("判断 相减差的数 是否为 float类型 "):
            if isinstance(result,float):
                with allure.step("相减差的数 为float类型，result 保留小数点后两位"):
                    result=round(result,2)
        with allure.step("断言 计算结果 等于 预期结果"):
            assert result==get_sub_datas_True[2]

    @allure.story("测试减法_无效测试用例")
    @pytest.mark.sub
    @pytest.mark.run(order=2)
    def test_sub_False(self,get_calc,get_sub_datas_False):
        with allure.step("计算两个数 相减差结果"):
            result=get_calc.sub(get_sub_datas_False[0],get_sub_datas_False[1])
        with allure.step("判断 相减差的数 是否为 float类型 "):
            if isinstance(result,float):
                with allure.step("相减差的数 为float类型，result 保留小数点后两位"):
                    result=round(result,2)
        with allure.step("断言 计算结果 不等于 预期结果"):
            assert result!=get_sub_datas_False[2]

    @allure.story("测试乘法_有效测试用例")
    @pytest.mark.mul
    @pytest.mark.run(order=3)
    def test_mul_True(self,get_calc,get_mul_datas_True):
        with allure.step("计算两个数 相乘积结果"):
            result=get_calc.mull(get_mul_datas_True[0],get_mul_datas_True[1])
        with allure.step("判断 相乘积的数 是否为 float类型 "):
            if isinstance(result,float):
                with allure.step("相乘积的数 为float类型，result 保留小数点后两位"):
                    result=round(result,2)
        with allure.step("断言 计算结果 等于 预期结果"):
            assert result==get_mul_datas_True[2]

    @allure.story("测试乘法_无效测试用例")
    @pytest.mark.mul
    @pytest.mark.run(order=3)
    def test_mul_False(self, get_calc, get_mul_datas_False):
        with allure.step("计算两个数 相乘积结果"):
            result=get_calc.mull(get_mul_datas_False[0],get_mul_datas_False[1])
        with allure.step("判断 相乘积的数 是否为 float类型 "):
            if isinstance(result,float):
                with allure.step("相乘积的数 为float类型，result 保留小数点后两位"):
                    result=round(result,2)
        with allure.step("断言 计算结果 等于 预期结果"):
            assert result!=get_mul_datas_False[2]






