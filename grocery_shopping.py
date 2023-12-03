#!/Users/MacBookPro-II/opt/anaconda3/bin/python
from foods import Food
from recipes import Recipe
from shopping_list import Shopping_list
import json
from pick import pick
from pprint import pprint

food_items_data = json.load(open("configs/food_items.json"))
dinner_recipes_data = json.load(open("configs/dinner_recipes.json"))
breakfast_recipes_data = json.load(open("configs/breakfast_recipes.json"))
weekly_items_data = json.load(open("configs/weekly_items.json"))
seldom_items_data = json.load(open("configs/seldom_items.json"))


food_items = {}
recipes = {}
breakfast_recipes = {}
weekly_items = []
seldom_items = []

# Loading in all of the food items from the json to the food class
for name, attributes in food_items_data.items():
    food = Food(name, attributes['department'], attributes['unit'])
    food_items[name] = food

# Loading all the recipes with food items
for name, attributes in dinner_recipes_data.items():
    items_in_recipe = []
    for item, quantity in attributes['ingredients']:
        items_in_recipe.append((food_items[item], quantity))
    recipes[name] = Recipe(name, items_in_recipe)

# Loading all breakfast recipes
for name, attributes in breakfast_recipes_data.items():
    items_in_breakfast_recipes = []
    for item, quantity in attributes['ingredients']:
        items_in_breakfast_recipes.append((food_items[item], quantity))
    breakfast_recipes[name] = Recipe(name, items_in_breakfast_recipes)

# converting weekly items to food items and loading them into the weekly list. 
for weekly_item, quantity in weekly_items_data:
    weekly_items.append((food_items[weekly_item], quantity))

# converting seldom items to food item objects
for seldom_item, quantity in seldom_items_data:
    seldom_items.append((food_items[seldom_item], quantity))


# Picking the dinner recipes that we need to add for the week.
weekly_recipes = []
last_selected = None
options = list(recipes.keys())
options.append("--Exit")
finished_adding_recipes = False
while not finished_adding_recipes:
    if last_selected == None:
        title = 'Please choose this weeks dinner recipes (ENTER to select): '
    else:
        title = 'I have added ' + last_selected + ' to the cart. \n So far I have: ' + str([x.name for x in weekly_recipes])
    selected, index = pick(options, title, multiselect=False)
    if selected == "--Exit":
        finished_adding_recipes = True
    else:
        weekly_recipes.append(recipes[selected])
        last_selected = selected
# print(weekly_recipes)

# Picking the breakfast recipes that we need to add for the week
weekly_breakfast_recipes = []
last_selected = None
options = list(breakfast_recipes.keys())
options.append("--Exit")
finished_adding_recipes = False
while not finished_adding_recipes:
    if last_selected == None:
        title = 'Please choose this weeks breakfast recipes (ENTER to select): '
    else:
        title = 'I have added ' + last_selected + ' to the cart. \n So far I have: ' + str([x.name for x in weekly_breakfast_recipes])
    selected, index = pick(options, title, multiselect=False)
    if selected == "--Exit":
        finished_adding_recipes = True
    else:
        weekly_breakfast_recipes.append(breakfast_recipes[selected])
        last_selected = selected

# Pick and Add the seldom items to grocery list
last_selected = None
seldom_items_data
options = [x[0].name for x in seldom_items]
options.append("--Exit")
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
  
# putting the dinner and breakfast recipes together
weekly_recipes = weekly_recipes + weekly_breakfast_recipes

# After we have picked our recipes for the week, and our seldom items we compile the shopping list for those items.
grocery_list = Shopping_list(weekly_recipes)
grocery_list.compile_recipe_list()
grocery_list.add_weekly_items(weekly_items)


# This is where I will call Adding the non-weekly items to the list
print("This weeks meals: ")
for x in weekly_recipes:
    print(x.name)


grocery_list.list_foods_by_department()
grocery_list.list_the_list()
