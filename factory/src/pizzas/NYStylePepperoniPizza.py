from pizzas.Pizza import Pizza

class NYStylePepperoniPizza(Pizza):
    @property
    def sauce(self):
        return "red sauce"

    @property
    def dough(self):
        return "deep dish crust"

    @property
    def toppings(self):
        return ["big ball of mozzerella cheese", "salami"]
