import json
store_department_list = json.load(open("configs/store_departments.json"))

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
        for dep in store_department_list:
            self.items_by_department[dep] = []
            for food_item, quantity in self.final_list.values():
                if dep == food_item.department:
                    self.items_by_department[dep].append((food_item.name, quantity, food_item.unit))
        # print("Final List by department", self.items_by_department)
    
    def list_the_list(self):
        print("I love you Cuppy Cup!")
        for dep in store_department_list:
            if self.items_by_department[dep]:
                print(" ")
                print(dep.upper())
            for entry in self.items_by_department[dep]:
                #print(entry)
                # ('black beans', 1, 'can')
                if entry[1] == 1:
                    print(entry[0] + " " + str(entry[1]) + " " + entry[2])
                else:
                    print(entry[0] + " " + str(entry[1]) + " " + entry[2]+"s")