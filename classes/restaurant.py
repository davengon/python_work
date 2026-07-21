class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Our restaurant is called: {self.restaurant_name}, and we work with {self.cuisine_type} cuisine!")
    
    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open!")

    def set_numer_served(self, new_customers):
        self.number_served = new_customers

    def increment_number_served(self, new_customers):
        self.number_served += new_customers

class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Bubble Gum", "Pistaccio", "Vanilla", "Blackberry sorbet"]
    
    def display_menu(self):
        print("These are our options: \n")
        for flavor in self.flavors:
            print(flavor)
        
        

my_restaurant = Restaurant("Lime Ceviche", "Peruvian")
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

second_restaurant = Restaurant("Coconut Water", "Puerto Rican")
third_restaurant = Restaurant("Shinto", "Japanese")
second_restaurant.describe_restaurant()
third_restaurant.describe_restaurant()

restaurant = Restaurant("Arepas y Arepas", "Colombian")
print(f"The restaurant has served {restaurant.number_served} customers")
restaurant.number_served = 10
print(f"The restaurant has served {restaurant.number_served} customers")
restaurant.set_numer_served(25)
print(f"The restaurant has served {restaurant.number_served} customers")
restaurant.increment_number_served(55)
print(f"The restaurant has served {restaurant.number_served} customers")

ice_cream_shop = IceCreamStand("Gellato", "Deserts")
ice_cream_shop.display_menu()

