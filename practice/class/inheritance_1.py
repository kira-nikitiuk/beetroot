# # Exercise 1: Online Store Inventory Management
# # Create a class hierarchy to represent an online store's 
# inventory management system. Start with a base class called 
# Product and include attributes such as name, price, and quantity. 
# Create subclasses for specific types of products, such as Electronics, 
# Clothing, and Books. Each subclass should have additional attributes and methods 
# specific to the type of product. Implement methods for adding new products, updating 
# quantities, and calculating total inventory value.

products = {
  "cd_player" : { "price" : 20, "quantity" : 45, "audio" : "yes", "video" : "no"},
  "dvd_player" : {"price" : 25, "quantity" : 55, "audio" : "yes", "video" : "yes"},
}

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def quantity_update():
        name = input("name of the product:")
        new_quantity = int(input("new quantiti of the product:"))
        products[name]["quantity"] = new_quantity
        print(products[name])



class Electronics(Product):
    def __init__(self, audio, video, name, price, quantity):
        super().__init__(name, price, quantity)
        self.audio = audio
        self.video = video

        


# class Clothing:

# class Books:               
        