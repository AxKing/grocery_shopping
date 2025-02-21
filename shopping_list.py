import json
store_department_list = json.load(open("configs/store_departments.json"))
produce_order_list = json.load(open("configs/aisle_food_order.json"))
aisle_food_order_list_dict = json.load(open("configs/aisle_food_order.json"))


class Shopping_list(object):
    def __init__(self, recipes):
        self.recipes = recipes
        self.final_list = {}
        self.items_by_department = {}
    def compile_recipe_list(self):
        # what do items look like?
        # Recipe objects- name, food items
        # loop through each recipe
            # loop through each food item and add it to the dictionary of final list
        for recipe in self.recipes:
            # this gives food objects and quantities
            # print(recipe.items)
            for item, quantity in recipe.items:
                if item.name not in self.final_list:
                    self.final_list[item.name]=[item, quantity]
                else:
                    self.final_list[item.name][1] += quantity
            # class Food(object) name, department, unit
        return self.final_list
        
        # For next time, we need to doctor the code below so that it grabs the food objects
        # and adds them to the final list or updates the quantities for Steve.
        # He suggests we do that in the main body of the function. 
    def add_weekly_items(self, weekly_items):
        for item, quantity in weekly_items:
            if item.name not in self.final_list:
                self.final_list[item.name]=[item, quantity]
            else:
                self.final_list[item.name][1] += quantity

    def list_foods_by_department(self):
        # thing.name, thing.department, thing.quantity, thing.unit
        # self.final_list -> dictionary "name": food_object, quantity
        list_of_ordered_aisle_keys = aisle_food_order_list_dict.keys()
        # print(list(list_of_ordered_aisle_keys))
        for dep in store_department_list:
            self.items_by_department[dep] = []
            for food_item, quantity in self.final_list.values():
                if dep == food_item.department:
                    self.items_by_department[dep].append((food_item.name, quantity, food_item.unit))
        # This fixes the order of the produce items.
        for dep in list_of_ordered_aisle_keys:
            if self.items_by_department[dep]:
                unordered_items = self.items_by_department[dep]
                ordered_items = sorted( 
                unordered_items,
                key=lambda item: aisle_food_order_list_dict[dep].index(item[0]))
                self.items_by_department[dep] = ordered_items
                if len(ordered_items) != len(unordered_items):
                    print("You're missing some items from the aisle_food_order.json file in the {dep}.")


    def list_the_list(self):
        for i in range(2):
            print("")
        print("I love you Cuppitty Cup Cup!")
        for dep in store_department_list:  
            if self.items_by_department[dep]:
                print(" ")
                print(dep.upper())
            for entry in self.items_by_department[dep]:
                print(entry[0] + " " + str(entry[1]) + " " + entry[2])


# for item in produce_order_list:
#     print(item)