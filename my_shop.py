class Shop:
    def __init__(self,shop_name) -> None:
        self.Shop_name = shop_name
        self.product_list = []

    def add_product(self,product):
        self.product_list.append(product)

    def product_details(self,product_id):
        for product in self.product_list:
            if product.id == product_id:
                return product
        return 'Can not found your Product,Please write the correct name of the product'
    
    def buy_product(self,product_name,price):
        for product in self.product_list:
            if product.name == product_name:
                if(product.price<=price):
                    self.product_list.remove(product)
                    extra = price - product.price
                    return (f'Here is your product,{product} and extra money:{extra}')
                else:
                    need = product.price - price
                    return (f'Please provide extra {need} money')
        return f'We can not found your product'

    def remove_product(self,product_id):
        for product in self.product_list:
            if product.id == product_id:
                self.product_list.remove(product)
                return (f'Here is your deleted product:{product}')
        print(f'Cant found your product')

    def all_products(self):
        for product in self.product_list:
            print(product)

class Product:
    product_id = 0
    def __init__(self,name,price,description,quantity,category) -> None:
        Product.product_id +=1
        self.name = name
        self.id = Product.product_id
        self.price = price
        self.description = description
        self.quantity = quantity
        self.category = category
    def __str__(self) -> str:
        return f"ID:{self.id},Name:{self.name},Price:{self.price},Description:{self.description},Quantity:{self.quantity},Category:{self.category}"

My_shop = Shop('A2S')
products = [
    Product("Laptop", 1200, "15-inch MacBook Pro", 10, "Electronics"),
    Product("Smartphone", 800, "iPhone 12", 15, "Electronics"),
    Product("Headphones", 150, "Wireless Bluetooth headphones", 20, "Electronics"),
    Product("T-shirt", 20, "Cotton T-shirt", 50, "Clothing"),
    Product("Jeans", 50, "Blue denim jeans", 30, "Clothing"),
    Product("Sneakers", 80, "Running shoes", 25, "Footwear"),
    Product("Backpack", 40, "Waterproof backpack", 20, "Accessories"),
    Product("Watch", 100, "Analog wristwatch", 30, "Accessories"),
    Product("Sunglasses", 30, "UV protection sunglasses", 40, "Accessories"),
    Product("Coffee Maker", 50, "Drip coffee maker", 15, "Appliances"),
    Product("Blender", 40, "Kitchen blender", 20, "Appliances"),
    Product("Toaster", 30, "Pop-up toaster", 25, "Appliances"),
    Product("Book", 10, "Bestseller novel", 100, "Books"),
    Product("Notebook", 5, "College-ruled notebook", 150, "Stationery"),
    Product("Pen", 1, "Blue ballpoint pen", 200, "Stationery"),
    Product("Desk Lamp", 20, "LED desk lamp", 30, "Home & Office"),
    Product("Mouse", 15, "Wireless computer mouse", 40, "Electronics"),
    Product("Keyboard", 30, "Mechanical gaming keyboard", 20, "Electronics"),
    Product("Power Bank", 25, "Portable charger", 30, "Electronics"),
    Product("Water Bottle", 10, "Stainless steel water bottle", 50, "Accessories")
]
for product in products:
    My_shop.add_product(product)

# My_shop.all_products()
# my_product = My_shop.product_details(13)
# my_product = My_shop.remove_product(13)
# print(my_product)
# by_product = My_shop.buy_product('Mouse',200)
# print(by_product)


