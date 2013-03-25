# Bar Guide

<<<<<<< HEAD
=======
# Copyright 2013 Tom Hanrahan
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License

>>>>>>> 0b02ac5d96336993e4c27920adf2aeecd4943d9f
# Bar Guide let's you:
#      Display the recipe for a drink
#      List all of the drinks in the recipe book
#      Add a new drink recipe
#      Delete a recipe
#      Edit a recipe
#      Quit when you're done

__version__ = 2.0

NAME = "name"
RECIPIE = "recipie"

import pickle, shelve

BAR_GUIDE = "bar_guide"

def formatted_input(part, question):
    """Gets a drink name, recipe or command and returns it properly formatted"""
    new_input = input(question)
    if part == NAME:
        new_input = new_input.title()
    elif part == RECIPIE:
        new_input = new_input.capitalize()
    else:
        print("Non-fatal error: Someting went wrong, but we'll proceed anyway\n")
    return new_input

# Main

print("Bartender's Guide to Drink Recipies\n")

# Read existing recipes from the Bar Guide book

drink_recipes = shelve.open(BAR_GUIDE, "c")

# Perform requested operations until 'done'

action = None

while action != "Done":
    action = formatted_input(NAME, "Enter <drink name>, 'list', 'add', 'delete', 'edit', or 'done': ")
    
    if action == "List":
        print("\n", list(drink_recipes.keys()), "\n")

    elif action == "Add":
        drink_name = formatted_input(NAME, "What drink do you want to add? ")
        if drink_name in drink_recipes:
            print("That drink is already in the recipe book.\n")
        else: 
            drink_recipe = formatted_input(RECIPIE, "What is the new recipe? ")
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
        drink_name = formatted_input(NAME, "What drink do you want to edit in the recipe book? ")
        if drink_name in drink_recipes:
            new_recipe = formatted_input(RECIPIE, "What is your new recipe? ")
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
        
        

