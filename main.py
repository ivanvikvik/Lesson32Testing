from entity.milk import Milk
from entity.bread import Bread
from entity.orange import Orange
from container.basket import Basket


def main():
    basket = Basket()

    br = Bread()
    o = Orange()
    m = Milk(1, 4.2, 5.5)

    basket.add(br)
    basket.add(o)
    basket.add(m)

    print(f"size = {basket.size}")

    print(basket)


if __name__ == "__main__":
    main()
