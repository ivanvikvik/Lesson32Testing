from entity.milk import Milk
from entity.bread import Bread
from entity.orange import Orange
from container.basket import Basket
from logic.shop_assistance import ShopAssistance


def main():
    basket = Basket()

    br = Bread("white", "second", 3.0)
    o = Orange(200, 3000, 1.5)
    m = Milk(1, 4.2, 5.5)

    basket.add(br)
    basket.add(o)
    basket.add(m)

    print(basket)

    total = ShopAssistance.calculate_total_price(basket)

    print(f"Total price is {total}")


if __name__ == "__main__":
    main()
