from entity.product import Product
from container.basket import Basket


class ShopAssistance:
    @staticmethod
    def calculate_total_price(basket):
        if isinstance(basket, Basket) and basket.size != 0:
            total = 0
            for i in range(basket.size):
                product = basket.get_product(i)

                if isinstance(product, Product):
                    total += product.price

            return total
