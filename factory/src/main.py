from pizza_store.LAPizzaStore import LAPizzaStore
from pizza_store.NYPizzaStore import NYPizzaStore


if __name__=="__main__":
    pizza_shop_ny = NYPizzaStore()
    pizza_shop_ny.order_pizza(type="cheese")

    pizza_shop_la = LAPizzaStore()
    pizza_shop_la.order_pizza(type="cheese")
