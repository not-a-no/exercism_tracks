"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    for item in items_to_add:
        if item in current_cart.keys():
            current_cart[item] += 1
        else:
            current_cart.setdefault(item, 1)
    return current_cart


def read_notes(notes):
    return dict.fromkeys(notes, 1)


def update_recipes(ideas, recipe_updates):
    ideas |= recipe_updates
    return ideas


def sort_entries(cart):
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    sent = {}
    sorted_cart = dict(sorted(cart.items()))
    for key in reversed(sorted_cart.keys()):
        sent[key] = [sorted_cart[key]] + aisle_mapping[key]
    return sent
        


def update_store_inventory(fulfillment_cart, store_inventory):
    for key in fulfillment_cart.keys():
        store_inventory[key][0] -= fulfillment_cart[key][0]
        if store_inventory[key][0] <= 0:
            store_inventory[key][0] = 'Out of Stock'
    return store_inventory
