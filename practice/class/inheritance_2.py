# product = {
#   "cd_player" : { "price" : 20, "quantity" : 45, "audio" : "yes", "video" : "no"},
#   "dvd_player" : {"price" : 25, "quantity" : 55, "audio" : "yes", "video" : "yes"},

# } 

# product["cd_player"]["price"] = 200
# print(product["cd_player"])

# name = "cd_player"
# new_quantity = 600

# product[name]["quantity"] = new_quantity
# print(product["cd_player"])

# def quantity_update():
#     name = input("name of the product:")
#     new_quantity = int(input("new quantiti of the product:"))
#     product[name]["quantity"] = new_quantity
#     print(product[name])

# quantity_update()    

# product["cd_player"].update({"color": "red"}) 

# print(product)

# def adding_product_electronic():
#     name = input("name of the product:")
#     price = input("price of the product:")
#     quantity = int(input("quantiti of the product:"))
#     audio = input("audio (yes\\no):") 
#     video = input("video (yes\\no):")
    
#     product[name].update({"price" : price, "quantity" : quantity, "audio" : audio, "video" : video })

# adding_product_electronic()

# def adding_product_electronic():
#     name = input("name of the product:")
#     price = input("price of the product:")
#     quantity = int(input("quantiti of the product:"))
#     audio = input("audio (yes\\no):") 
#     video = input("video (yes\\no):")
    
#     product[name].update({"price" : price, "quantity" : quantity, "audio" : audio, "video" : video })






def new_products(self):  
        new_dict = {
            "name" : self.name,
            "price" : self.price,
            "quantity" : self.quantity
            
        }
        return new_dict    

















