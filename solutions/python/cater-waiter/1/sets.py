"""Functions for compiling dishes and ingredients for a catering company."""

from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    return (dish_name, set(dish_ingredients))

def check_drinks(drink_name, drink_ingredients):
    if set(drink_ingredients).isdisjoint(ALCOHOLS):
        return drink_name + " Mocktail"
    return drink_name + " Cocktail"

def categorize_dish(dish_name, dish_ingredients):
    if set(dish_ingredients) <= VEGAN:
        return dish_name+": VEGAN"
    if set(dish_ingredients) <= VEGETARIAN:
        return dish_name+": VEGETARIAN"    
    if set(dish_ingredients) <= PALEO:
        return dish_name+": PALEO"    
    if set(dish_ingredients) <= KETO:
        return dish_name+": KETO"   
    if set(dish_ingredients) <= OMNIVORE:
        return dish_name+": OMNIVORE"


def tag_special_ingredients(dish):
    return (dish[0], set(dish[1]) & SPECIAL_INGREDIENTS)



def compile_ingredients(dishes):
    master = set()
    for i in range(len(dishes)):
        master = master | dishes[i]
    return master


def separate_appetizers(dishes, appetizers):
    return list(set(dishes) - set(appetizers))


def singleton_ingredients(dishes, intersection):
    all_ingredients = set().union(*dishes)  # union of all dishes
    repeated = set()  # ingredients that appear in 2+ dishes
    
    for i, dish in enumerate(dishes):
        for other in dishes[i+1:]:
            repeated |= dish & other  # intersection finds repeated ones

    # Singleton = all ingredients - repeated ones - category-wide intersection
    return all_ingredients - repeated - intersection
