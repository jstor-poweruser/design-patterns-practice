from abc import ABC, abstractmethod


class Pizza(ABC):
    """Python doesn't provide abstract classes by default, but they offer a module called ABC that allows you to define abstract classes.
       Only one of these methods, the createPizza method, needs to be abstract, because that's the only method that may differ depending on
       what kind of pizza we make. All other methods, like baking, cutting, and boxing the pizzas will remain the same."""
    def __init__(self):
        pass

    @property
    @abstractmethod
    def sauce(self):
        """These are abstract because different kinds of pizzas need different kinds of sauce/dough, but once the subclass defines them I don't want to change them, hence no setters"""
        pass
    
    @property
    @abstractmethod
    def dough(self):
        pass

    @property
    @abstractmethod
    def toppings(self):
        return []

    def bake(self):
        print("I'm baking for 20 minutes at 450!")

    def cut(self):
        print("10 slices!")

    def box(self):
        print("I'm being put in a box!")

    def prepare(self):
        print(f"Preparing pizza with {self.sauce} and {self.dough}")
        print(f"Adding toppings such as {(', '.join(self.toppings))}")
