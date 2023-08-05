# Task 3
# Product Store
# Write a class Product that has three attributes:
# type
# name
# price
# Then create a class ProductStore, which will have some Products and will operate with all products in the store. All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
# Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement additional classes to operate on a certain type of product, etc.
# Also, the ProductStore class must have the following methods:
# add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
# set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers (type or name). The discount must be specified in percentage
# sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error. It also increments income if the sell_product method succeeds.
# get_income() - returns amount of many earned by ProductStore instance.
# get_all_products() - returns information about all available products in the store.
# get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
'''
class Product:
    pass
class ProductStore:
    pass
p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product(Food, 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell('Ramen', 10)
assert s.get_product_info('Ramen') == ('Ramen', 290)
'''


class Product:
    def __init__(self, type, name, price):
        #self.product = {"type": type, "name": name, "price": price}
        self.type = type
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
        self.products = []
        self.income = 0

    def add(self, product, amount):
        if not isinstance(product, Product):
            raise  ValueError ("немає такого продукту!")
        self.products.append({"product": product, "amount": amount})

    def set_discount(self, identifier, percent, identifier_type = 'name'):
        if identifier_type not in ['type', 'name']:
            raise ValueError("невірний тип ідентифікатора")
        for item in self.products:
            if identifier_type == 'type' and item['product'].type == identifier:
                item['product'].price *= (1 - percent / 100)
            elif identifier_type == 'name' and item['product'].name == identifier:
                item['product'].price *= (1 - percent / 100)       

    def sell_product(self, product_name, amount):
        for item in self.products:
            if item['product'].name == product_name:
                if item['amount'] >= amount:
                    item['amount'] -= amount
                    self.income += item['product'].price * amount
                    return
                else:
                    raise ValueError("недостатньо товар уна складі")
        raise ValueError("продукт не знайдено")

    def get_income(self):
        return self.income

    def get_all_products(self):
        return [(item['product'].type, item['product'].name, item['product'].price, item['amount']) for item in self.products]

    def get_product_info(self, product_name):
        for item in self.products:
            if item['product'].name == product_name:
                return (item['product'].name, item['amount'])
        raise ValueError("продукт не знайдено")    



product1 = Product("Food", 'Ramen', 1.5)
product2 = Product('Sport', 'Football T-Shirt', 100)
product3 = Product("Electronics", "Notebook", 1500)

store = ProductStore()

store.add(product1, 10)
store.add(product2, 300)
store.add(product3, 5)

store.set_discount("Electronics", 10, identifier_type = "type")
store.set_discount('Football T-Shirt', 15)

store.sell_product('Ramen', 10)

print("income:", store.get_income())
print("all products:", store.get_all_products())
print("information about product:", store.get_product_info('Ramen'))

        
            
