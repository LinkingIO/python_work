import unittest

def return_city_country(city, country):
    """返回城市国家名称"""
    city_country = city.title() + ', ' + country.title()
    return city_country

def return_city_country_v2(city, country, population=0):
    """返回城市国家名称和人口"""
    if population:
        city_country = city.title() + ', ' + country.title() + " - population " + str(population)
    else:
        city_country = city.title() + ', ' + country.title()
    return city_country

class TestCityCountry(unittest.TestCase):
    """一个测试城市国家名称的类"""

    def test_city_country(self):
        """一个测试的方法"""
        city_country = return_city_country('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')

    def test_city_country_v2(self):
        """一个测试的方法"""
        city_country = return_city_country_v2('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')

    def test_city_country_v3(self):
        """一个测试的方法"""
        city_country = return_city_country_v2('santiago', 'chile', population=5000000)
        self.assertEqual(city_country, 'Santiago, Chile - population 5000000')

unittest.main()