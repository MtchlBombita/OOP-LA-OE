print("LA:18")
class Favoritefood():
    def __init__(self, bun, patty, cheese, toppings):
        self.bun = bun
        self.patty = patty
        self.cheese = cheese
        self.toppings = toppings

    def __str__(self):
        toppings_str = ', '.join(self.toppings) if self.toppings else "No toppings"
        return f"A burger with a {self.bun} bun, {self.patty} patty, {self.cheese} cheese, topped with {toppings_str}."

burger1 = Favoritefood("Sesame", "Beef", "Cheddar", ["Lettuce", "Tomato", "Pickles"])
burger2 = Favoritefood("Whole Wheat", "Chicken", "Swiss", ["Avocado", "Onions", "Bacon"])
burger3 = Favoritefood("Pretzel", "Veggie", "American", ["Mushrooms", "Spinach", "Mustard"])

print(burger1)
print(burger2)
print(burger3)
