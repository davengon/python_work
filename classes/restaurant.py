class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Our restaurant is called: {self.restaurant_name}, and we work with {self.cuisine_type} cuisine!")
    
    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open!")

my_restaurant = Restaurant("Lime Ceviche", "Peruvian")
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

second_restaurant = Restaurant("Coconut Water", "Puerto Rican")
third_restaurant = Restaurant("Shinto", "Japanese")
second_restaurant.describe_restaurant()
third_restaurant.describe_restaurant()