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
    """
    Categorize a dish based on its ingredients.

    Args:
        dish_name (str): The name of the dish.
        dish_ingredients (iterable): The list or set of ingredients in the dish.

    Returns:
        str: A string in the format "<dish_name>: <CATEGORY>" where CATEGORY
             is one of VEGAN, VEGETARIAN, PALEO, KETO, OMNIVORE, or UNKNOWN.
    """
    dish_set = set(dish_ingredients)
    categories = {
        "VEGAN": VEGAN,
        "VEGETARIAN": VEGETARIAN,
        "PALEO": PALEO,
        "KETO": KETO,
        "OMNIVORE": OMNIVORE
    }
    for name, category_set in categories.items():
        if dish_set <= category_set:
            return f"{dish_name}: {name}"
    return f"{dish_name}: UNKNOWN"



def tag_special_ingredients(dish):
    return (dish[0], set(dish[1]) & SPECIAL_INGREDIENTS)


def compile_ingredients(dishes):
    return set().union(*dishes)


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
