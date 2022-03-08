from pizza_store.PizzaStore import PizzaStore
from pizzas.NYStyleCheesePizza import NYStyleCheesePizza
from pizzas.NYStylePepperoniPizza import NYStylePepperoniPizza
from pizzas.Pizza import Pizza

class NYPizzaStore(PizzaStore):
    def _create_pizza(self, type) -> Pizza:
        if (type == "cheese"):    
            return NYStyleCheesePizza()
        elif (type == "pepperoni"):
            return NYStylePepperoniPizza()
        else:
            print("Hey! No Pizza?")
