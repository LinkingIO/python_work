# 9.1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # 9.4
        self.number_served = number_served

    def describe_restaurant(self):
        """描述餐厅的属性"""
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        """餐厅开业"""
        print("The restaurant is servicing")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, incre_served):
        """就餐人数递增"""
        self.number_served += incre_served
