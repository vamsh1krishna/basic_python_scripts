def food_items(*args):
    """
    args:
        multiple strings as arguments
    return:
        example for arguments
        food_items('salad')  ====> You are bringing salad
        food_items('salad','chips)  ====> You are bringing salad and chips
        food_items('salad','chips','cake')  ====> You are bringing salad,chips and cake
    """
    if len(args) ==1:
        op = f"You are bringing {args[0]}"
    elif len(args) ==2:
        op = f"You are bringing {args[0]} and {args[1]}"
    elif len(args)>2:
        last_two = f"{args[-2]} and {args[-1]}"
        remaining_elements = ', '.join(args[:-2])
        op = f"You are bringing {remaining_elements}, {last_two}"
    return op

print(food_items('salad'))
print(food_items('salad','chips'))
print(food_items('salad','chips','cake'))
print(food_items('salad','chips','cake','muffin'))

