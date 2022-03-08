from pizzas.Pizza import Pizza

class LAStylePepperoniPizza(Pizza):
    @property
    def sauce(self):
        return "liberal sauce"

    @property
    def dough(self):
        return "thin crust"

    @property
    def toppings(self):
        return ["feta", "vegan pepperoni"]
