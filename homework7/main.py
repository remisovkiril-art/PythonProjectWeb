from product_mixins import ProductManager


product = ProductManager("Laptop", 1000)

product.log("Product created")
print("Product:", product.name)
print("Original price:", product.price, "UAH")

product.apply_discount(15)

print("Price after discount:", product.price, "UAH")
print("Product JSON:", product.to_json())

product.log("Discount applied")

print("Method Resolution Order:")
print(ProductManager.mro())
