# Bar Guide

# Bar Guide let's you:
#      Display the recipe for a drink
#      List all of the drinks in the recipe book
#      Add a new drink recipe
#      Delete a recipe
#      Edit a recipe
#      Quit when you're done

__version__ = 1.0

import pickle, shelve

BAR_GUIDE = "bar_guide"

def formatted_input(question):
    """Gets a drink name, recipe or command and returns it properly formatted"""
    new_input = input(question)
    new_input = new_input.title()
    return new_input

# Main

print("Bartender's Guide to Drink Recipies\n")

# Read existing recipes from the Bar Guide book

drink_recipes = shelve.open(BAR_GUIDE, "c")

# Perform requested operations until 'done'

action = None

while action != "Done":
    action = formatted_input("Enter <drink name>, 'list', 'add', 'delete', 'edit', or 'done': ")
    
    if action == "List":
        print("\n", list(drink_recipes.keys()), "\n")

    elif action == "Add":
        drink_name = formatted_input("What drink do you want to add? ")
        if drink_name in drink_recipes:
            print("That drink is already in the recipe book.\n")
        else: 
            drink_recipe = formatted_input("What is the new recipe? ")
            drink_recipes[drink_name] = drink_recipe
            print(drink_name, "recipe added to the recipe book\n")
            
    elif action == "Delete":
        drink_name = formatted_input("What drink do you want to delete from the recipe book? ")
        if drink_name in drink_recipes:
            del drink_recipes[drink_name]
            print(drink_name, "entry deleted\n")
        else:
            print(drink_name, "not found\n")
            
    elif action == "Edit":
        drink_name = formatted_input("What drink do you want to edit in the recipe book? ")
        if drink_name in drink_recipes:
            new_recipe = formatted_input("What is your new recipe? ")
            drink_recipes[drink_name] = new_recipe
            print(drink_name, "entry changed to ")
            print(drink_recipes.get(drink_name), "\n")
        else:
            print(drink_name, "not found\n")
            
    elif action == "Done":
        drink_recipes.close()
        print("Adios, my friend\n")
   
    #Assume that 'action' is a drink name that has been entered
    else:
        print(drink_recipes.get(action, "I don't know that recipe"), "\n")
        
        

