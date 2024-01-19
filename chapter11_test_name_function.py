def get_formatted_name(first, last):
    """生成简洁的姓名"""
    full_name = first + ' ' + last
    return full_name.title()


import unittest

class NamesTestCase(unittest.TestCase):
    """测试get_formatted_name function"""

    def test_first_last_name(self):
        """是否能正确处理Janis Joplin这样的姓名"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()