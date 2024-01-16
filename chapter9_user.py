
class ModelUser():
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
    
    def show_name(self):
        print("First name: " + self.first_name)
        print("Last name: " + self.last_name)

class ModelPrivileges():
    def __init__(self, privileges = ['can add post', 'can delete post', 'can ban user']) -> None:
        self.privileges = privileges

    def show_privileges(self):
        print(",".join(self.privileges))

class ModelAdmin(ModelUser):
    def __init__(self, first_name, last_name) -> None:
        super().__init__(first_name, last_name)
        self.privileges = ModelPrivileges()
    

