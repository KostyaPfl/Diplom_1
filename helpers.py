
def get_available_items_names(items):
    available_items_names = [item.name for item in items]
    return available_items_names


def validate_items_class(items_list, expected_class) -> bool:
    return all(isinstance(item, expected_class) for item in items_list)
