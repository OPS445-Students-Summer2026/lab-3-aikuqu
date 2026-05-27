#!/usr/bin/env python3

# Place my_list below this comment (before the function definitions)

my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    # Appends new item to end of list with the value (last item + 1)
    cool_value = ordered_list[-1] + 1 # store the value in cool_value variable
    ordered_list.append(cool_value) # append the value
    return ordered_list # return the value


def remove_items_from_list(ordered_list, items_to_remove):
    # Removes all values, found in items_to_remove list, from ordered_list
    for item in items_to_remove: # for item in the items_to_remove list
        if item in ordered_list: # if number is in list
            ordered_list.remove(item) # remove number from list aka item


def remove_item(list_1, number_remove):
    for num in list_1:
        if number_remove in list_1:
            list_1.remove(number_remove)

# Main code
if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1,5,6])
    print(my_list)
    remove_item(my_list, [5,4,3])
    print(my_list)

