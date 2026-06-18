class Product:
    def __init__(self, product_name='', product_code=0):
        self.product_name = product_name
        self.product_code = product_code

product_name, product_code = input().split()
product_code = int(product_code)

product1 = Product()
product2 = Product(product_name, product_code)

product1.product_name = 'codetree'
product1.product_code = 50

print(f'product {product1.product_code} is {product1.product_name}')
print(f'product {product2.product_code} is {product2.product_name}')