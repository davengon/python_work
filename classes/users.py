class User:

    def __init__(self, first_name, last_name, phone_number, id):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.id = id
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"The user's name is: {self.first_name + " " + self.last_name}, their phone number is {self.phone_number}, and their id is: {self.id}")
    
    def greet_user(self):
        print(f"Hello, {self.first_name}, welcome back!")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):

    def __init__(self, first_name, last_name, phone_number, id):
        super().__init__(first_name, last_name, phone_number, id)
        self.priviliges = Privilites()
    


class Privilites():

    def __init__(self):
        self.priviliges = ["Can add post", "Can delete post", "can edit post"]
    
    def show_priviliges(self):
        print("These are your priviliges: \n")
        for power in self.priviliges:
            print(power)
        

first_user = User("David", "Gallego", "154654654", "0001")
second_user = User("Santiago", "Gal", "464564654", "0002")

first_user.greet_user()
first_user.describe_user()
second_user.greet_user()
second_user.describe_user()

first_user.increment_login_attempts()
first_user.increment_login_attempts()
print(first_user.login_attempts)
first_user.reset_login_attempts()
print(first_user.login_attempts)

new_admin = Admin("David", "Gallego", "2224", "00001")
new_admin.priviliges.show_priviliges()

