class Shopping_list(object):
    def __init__(self, recipes):
        self.recipes = recipes
        self.final_list = {}
    def compile_list(self):
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
