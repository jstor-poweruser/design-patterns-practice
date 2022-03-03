from pizzas.Pizza import Pizza

class NYStyleCheesePizza(Pizza):
    def get_sauce(self):
        return "liberal sauce"

    def get_dough(self):
        return "thin crust"

    def get_toppings(self):
        return ["feta cheese"]
