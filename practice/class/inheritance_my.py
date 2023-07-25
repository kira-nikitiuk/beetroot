class Product:
    def __init__(self, name, price, quantity): # створили дікти 
        self.name = name
        self.price = price
        self.quantity = quantity


    def quantity_update(self):  # зміна кількості
        self.name = input("name of the product:")
        new_quantity = int(input("new quantiti of the product:"))
        self.quantity = new_quantity


    def make_dict(self):  # робимо словник
        my_dict = {
            "name" : self.name,
            "price" : self.price,
            "quantity" : self.quantity
        }
        return my_dict


class Electronics(Product):
    def __init__(self, name, price, quantity, audio, video):
        super().__init__(name, price, quantity)
        self.audio = audio
        self.video = video


    def make_dict_for_electronics(self):
        my_dict_electronics = {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "audio": self.audio,
            "video": self.video
        }
        return my_dict_electronics



class Clothing(Product):
    def __init__(self, name, price, quantity, material, color):
        super().__init__(name, price, quantity)
        self.material = material
        self.color = color

    


# class Books(Product):

    
# pr1 = Product("cd", 20, 34)
# print(pr1.make_dict())
# pr1.quantity_update()
# print(pr1.make_dict())

new_electronics = Electronics("New Electronics", 100, 5, "н", "y")
print(new_electronics.make_dict())