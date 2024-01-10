def build_person(first_name, last_name, age = 0):
    """返回 dict，包含一个人的信息"""
    person = {"first_name": first_name, "last_name": last_name}
    if age:
        person["age"] = age
    return person
