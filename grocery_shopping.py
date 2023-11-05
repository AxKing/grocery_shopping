#!/Users/MacBookPro-II/opt/anaconda3/bin/python
from foods import Food
from recipes import Recipe
import json

food_items_data = json.load(open("configs/food_items.json"))
recipes_data = json.load(open("configs/recipes.json"))

food_items = {}
recipes = {}

# Loading in all of the food items from the json to the food class
for name, attributes in food_items_data.items():
    food = Food(name, attributes['department'], attributes['unit'])
    food_items[name] = food

for name, attributes in recipes_data.items():
    items_in_recipe = []
    for item, quantity in attributes['ingredients']:
        items_in_recipe.append((food_items[item], quantity))
    recipes[name] = Recipe(name, items_in_recipe)

print(food_items['butter'].unit)
print(recipes)
