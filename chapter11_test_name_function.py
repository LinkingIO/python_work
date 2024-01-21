import unittest

def get_formatted_name(first, last):
    """生成简洁的姓名"""
    full_name = first + ' ' + last
    return full_name.title()

# class NamesTestCase(unittest.TestCase):
#     """测试get_formatted_name function"""

#     def test_first_last_name(self):
#         """是否能正确处理Janis Joplin这样的姓名"""
#         formatted_name = get_formatted_name('janis', 'joplin')
#         self.assertEqual(formatted_name, 'Janis Joplin')

# unittest.main()

def get_formatted_name_v1(first, middle, last):
    """生成完整姓名"""
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()

# class NamesTestCaseV1(unittest.TestCase):
#     """测试get_formatted_name function"""

#     def test_first_last_name_v1(self):
#         """是否能正确处理Janis Joplin这样的姓名"""
#         formatted_name = get_formatted_name_v1('janis', 'joplin')
#         self.assertEqual(formatted_name, 'Janis Joplin')

# unittest.main()

def get_formatted_name_v2(first, last, middle=''):
    """生成完整姓名"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

class NamesTestCaseV2(unittest.TestCase):
    """测试get_formatted_name function"""

    def test_first_last_name_v2(self):
        """是否能正确处理Janis Joplin这样的姓名"""
        formatted_name = get_formatted_name_v2('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_last_middle_name(self):
        """能否正确处理Wolf Amadeus Mozart 这样的名字"""
        formated_name = get_formatted_name_v2('wolf', 'mozart', 'amadeus')
        self.assertEqual(formated_name,'Wolf Amadeus Mozart')

unittest.main()

