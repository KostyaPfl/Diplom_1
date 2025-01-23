
def get_available_ingredient_names(ingredients):
    available_ingredient_names = [ingredient.name for ingredient in ingredients]
    return available_ingredient_names


def validate_items_class(items_list, expected_class) -> bool:
    return all(isinstance(item, expected_class) for item in items_list)
