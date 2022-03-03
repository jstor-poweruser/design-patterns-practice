from PizzaStore import PizzaStore
from pizzas.NYStyleCheesePizza import NYStyleCheesePizza
from pizzas.Pizza import Pizza

class NYPizzaStore(PizzaStore):
    def _create_pizza(self, type) -> Pizza:
        if (type == 'cheese'):    
            return NYStyleCheesePizza()
        else:
            print("Hey! No Pizza?")


if __name__=="__main__":
    pizza_shop = NYPizzaStore()
    pizza_shop.order_pizza(type='cheese')
