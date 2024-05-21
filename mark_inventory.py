from typing import List


def mark_inventory(clothing_items: List[str]) -> List[str]:
    """
    Marks the inventory of clothing items with different sizes.

    Args:
        clothing_items (List[str]): A list of clothing items.

    Returns:
        List[str]: A list of marked clothing options with sizes.

    """
     
    clothing_options = []

    for item in clothing_items:
        for size in range(1, 6):
            clothing_options.append(item + " Size: " + str(size))

    return clothing_options


print(mark_inventory(["Purple Shirt", "Green Shirt"]))