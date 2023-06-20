class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
    def open_restaurant(self):
        print(f"The restaurant, {self.restaurant_name} is now open")

my_restaurant1 = Restaurant("Golden Pizza", "American")
my_restaurant2 = Restaurant("Golden Fork", "Japanese")
my_restaurant3 = Restaurant("Fishworks", "British")

class User:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")



User1 = User("Joseph", "Thanos", 27)
User2 = User("Hana", "Sam", 17)
User3 = User("Smith", "Jacob",16) 

User1.describe_user()
User1.greet_user()
print("")

User2.describe_user()
User2.greet_user()
print("")
User3.describe_user()
User3.greet_user()
print("")

my_restaurant1.describe_restaurant()
print("")
my_restaurant2.describe_restaurant()
print("")
my_restaurant3.describe_restaurant()
print("")


