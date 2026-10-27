from product import Product


class ProductModel:
    def __init__(self):
        self.products = [
            Product(
                "Банани",
                "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?auto=format&fit=crop&w=500&q=80",
                45,
                4.8
            ),
            Product(
                "Яблука",
                "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?auto=format&fit=crop&w=500&q=80",
                35,
                4.7
            ),
            Product(
                "Апельсини",
                "https://images.unsplash.com/photo-1547514701-42782101795e?auto=format&fit=crop&w=500&q=80",
                55,
                4.9
            ),
            Product(
                "Полуниця",
                "https://images.unsplash.com/photo-1464965911861-746a04b4bca6?auto=format&fit=crop&w=500&q=80",
                120,
                4.8
            ),
            Product(
                "Чорниця",
                "https://images.unsplash.com/photo-1498557850523-fd3d118b962e?auto=format&fit=crop&w=500&q=80",
                150,
                4.9
            ),
            Product(
                "Виноград",
                "https://images.unsplash.com/photo-1537640538966-79f369143f8f?auto=format&fit=crop&w=500&q=80",
                95,
                4.6
            ),
            Product(
                "Ківі",
                "https://images.unsplash.com/photo-1618897996318-5a901fa6ca71?auto=format&fit=crop&w=500&q=80",
                80,
                4.7
            ),
            Product(
                "Манго",
                "https://images.unsplash.com/photo-1553279768-865429fa0078?auto=format&fit=crop&w=500&q=80",
                140,
                4.8
            )
        ]

    def get_all_products(self):
        return self.products

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product

        return None

    def create_product(self, product):
        self.products.append(product)
        return product
