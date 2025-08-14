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
    dish_set = set(dish_ingredients)
    categories = {
        "VEGAN": VEGAN,
        "VEGETARIAN": VEGETARIAN,
        "PALEO": PALEO,
        "KETO": KETO,
        "OMNIVORE": OMNIVORE
    }
    for name, category_set in categories.items():
        if dish_set <= category_set:  # subset check
            return f"{dish_name}: {name}"


def tag_special_ingredients(dish):
    return (dish[0], set(dish[1]) & SPECIAL_INGREDIENTS)



def compile_ingredients(dishes):
    master = set()
    for ii, dish in enumerate(dishes):
        master = master | dishes[ii]
    return master


def separate_appetizers(dishes, appetizers):
    return list(set(dishes) - set(appetizers))


def singleton_ingredients(dishes, intersection):
    all_ingredients = set().union(*dishes)  # union of all dishes
    repeated = set()  # ingredients that appear in 2+ dishes
    
    for ii, dish in enumerate(dishes):
        for other in dishes[ii+1:]:
            repeated |= dish & other  # intersection finds repeated ones

    # Singleton = all ingredients - repeated ones - category-wide intersection
    return all_ingredients - repeated - intersection
