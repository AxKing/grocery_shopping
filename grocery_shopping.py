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
seldom_items_data = json.load(open("configs/seldom_items.json"))

food_items = {}
recipes = {}
weekly_items = []
seldom_items = []

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

# converting seldom items to food item objects
for seldom_item, quantity in seldom_items_data:
    seldom_items.append((food_items[seldom_item], quantity))


# Picking the recipes that we need to add for the week.
weekly_recipes = []
last_selected = None
options = list(recipes.keys())
options.append("--Exit")
# print(options)
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

#
"""
1. list the seldom items
2. add the items to the "Weekly Items List"
"""
last_selected = None
seldom_items_data
options = [x[0].name for x in seldom_items]
options.append("--Exit")
# print(options)
finished_adding_seldom_items = False
while not finished_adding_seldom_items:
    if last_selected == None:
        title = 'Do you need any of these for this trip? (ENTER to select): '
    else:
        title = 'I have added ' + last_selected + ' to the cart.'
    selected, index = pick(options, title, multiselect=False)
    
    if selected == "--Exit":
        finished_adding_seldom_items = True
    else:
        weekly_items.append(seldom_items[index])
        last_selected = selected
  

# After we have picked our recipes for the week, we compile the shopping list for those items.
grocery_list = Shopping_list(weekly_recipes)
grocery_list.compile_recipe_list()
grocery_list.add_weekly_items(weekly_items)


# This is where I will call Adding the non-weekly items to the list

grocery_list.list_foods_by_department()
grocery_list.list_the_list()
