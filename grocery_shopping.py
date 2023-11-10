#!/Users/MacBookPro-II/opt/anaconda3/bin/python
from foods import Food
from recipes import Recipe
from shopping_list import Shopping_list
import json
from pprint import pprint
from pick import pick

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


# Picking the recipes that we need to add for the week.
weekly_recipes = []
last_selected = None
options = list(recipes.keys())
options.append("--Exit")
print(options)
finished_adding_recipes = False
while not finished_adding_recipes:
    if last_selected == None:
        title = 'Please choose this weeks recipes (ENTER to select): '
    else:
        title = 'I have added ' + last_selected + ' to the cart.'
    selected, index = pick(options, title, multiselect=False)
    if selected == "--Exit":
        finished_adding_recipes = True
    else:
        weekly_recipes.append(recipes[selected])
        last_selected = selected
print(weekly_recipes)

grocery_list = Shopping_list(weekly_recipes)
grocery_list.compile_list()
pprint(grocery_list.final_list)


# final_list = add_weekly_items(grocery_list)
# print(final_list)
