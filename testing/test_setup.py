def setup_module():
    print("模块级别的 setup(最高级)")
def teardown_module():
    print("模块级别的 teardown(最高级)")


def setup_function():
    print("函数级别的 setup(函数在类外)")
def teardown_function():
    print("函数级别的 teardown(函数在类外)")
def test_func1():
    print("测试函数1")


class TestDemo:
    def setup_class(self):
        print("类级别的 setup")
    def teardown_class(self):
        print("类级别的 teardown")

    def setup(self):
        print("方法级别的 setup")
    def teardown(self):
        print("方法级别的 teardown")
    def test_demo1(self):
        print("test_demo1 打印提示")
    def test_demo2(self):
        print("test_demo2 打印提示")

class TestDemo2:
    def setup_class(self):
        print("类级别的 setup")
    def teardown_class(self):
        print("类级别的 teardown")

    def setup(self):
        print("方法级别的 setup")
    def teardown(self):
        print("方法级别的 teardown")
    def test_demo1(self):
        print("test_demo1 打印提示")
    def test_demo2(self):
        print("test_demo2 打印提示")






