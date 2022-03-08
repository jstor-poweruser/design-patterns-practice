from pizza_store.PizzaStore import PizzaStore
from pizzas.LAStyleCheesePizza import LAStyleCheesePizza
from pizzas.LAStylePepperoniPizza import LAStylePepperoniPizza
from pizzas.Pizza import Pizza

class LAPizzaStore(PizzaStore):
    def _create_pizza(self, type) -> Pizza:
        if (type == "cheese"):    
            return LAStyleCheesePizza()
        elif (type == "pepperoni"):
            return LAStylePepperoniPizza()
        else:
            print("Hey! No Pizza?")
