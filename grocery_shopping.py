#!/Users/MacBookPro-II/opt/anaconda3/bin/python
from foods import Food
from recipes import Recipe
from shopping_list import Shopping_list
import json
from pprint import pprint
from pick import pick

food_items_data = json.load(open("configs/food_items.json"))
recipes_data = json.load(open("configs/recipes.json"))
weekly_items_data = json.load(open("configs/weekly_items.json"))

food_items = {}
recipes = {}
weekly_items = []

# Loading in all of the food items from the json to the food class
for name, attributes in food_items_data.items():
    food = Food(name, attributes['department'], attributes['unit'])
    food_items[name] = food

# Loading all the recipes with food items
for name, attributes in recipes_data.items():
    items_in_recipe = []
    for item, quantity in attributes['ingredients']:
        items_in_recipe.append((food_items[item], quantity))
    recipes[name] = Recipe(name, items_in_recipe)

# converting weekly items to food items and loading them into the weekly list. 
for weekly_item, quantity in weekly_items_data:
    weekly_items.append((food_items[weekly_item], quantity))

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
# print(weekly_recipes)


# After we have picked our recipes for the week, we compile the shopping list for those items.
grocery_list = Shopping_list(weekly_recipes)
grocery_list.compile_recipe_list()
# Add the weekly
# Taking weekly items json and converting it to a weekly_items list of food/quantity touples
grocery_list.add_weekly_items(weekly_items)
grocery_list.list_foods_by_department()
# pprint(grocery_list.final_list)
grocery_list.list_the_list()

# final_list = add_weekly_items(grocery_list)
# print(final_list)
