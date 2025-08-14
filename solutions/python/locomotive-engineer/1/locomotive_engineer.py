"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    x, y, *last = each_wagons_id
    index_after1 = last.index(1) + 1
    last[index_after1:index_after1] = missing_wagons
    return last + [x, y]


def add_missing_stops(route, **kwargs):
    return {**route, "stops": list(kwargs.values())}


def extend_route_information(route, more_route_information):
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    return [list(group) for group in zip(*wagons_rows)]

