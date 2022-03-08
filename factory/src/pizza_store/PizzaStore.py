from abc import ABC, abstractmethod
from pizzas.Pizza import Pizza

class PizzaStore(ABC):
    """The PizzaStore class is also abstract because we need to be able to define different types of PizzaStore classes."""
    def __init__(self):
        pass

    @abstractmethod
    def _create_pizza(self, type: str):
        """We will be redefining the createPizza method depending on what kind of pizza we are making."""
        pass

    def order_pizza(self, type: str) -> Pizza:
        pizza = self._create_pizza(type=type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza