import unittest

class Employee():
    """存储雇员信息"""

    def __init__(self, last_name, first_name, annual_salary) -> None:
        """初始化对象接收名、姓和年薪"""
        self.last_name = last_name
        self.first_name = first_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_annual_salary = 5000):
        """提供一个增加年薪的方法，默认增加 5000"""
        self.annual_salary += raise_annual_salary

class TestEmployee(unittest.TestCase):
    """针对雇员的测试类"""

    def setUp(self) -> None:
        """创建雇员信息实例，仅初始化一次"""
        self.employee = Employee('dayo', 'yang', 100000)

    def test_give_default_raise(self):
        """增加默认年薪，进行测试"""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 105000)

    def test_give_custom_raise(self):
        """增加指定年薪，进行测试"""
        self.employee.give_raise(1000)
        self.assertEqual(self.employee.annual_salary, 101000)
        
unittest.main()