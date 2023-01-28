def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """

    if location == "beginning":
        index = 0
    elif location == "end":
        index = -1
    else:
        return None


    # command == remove, return removed item
    if command == "remove":
        value = lst[index]
        lst.remove(value)
        return value

    # command == add, return list
    elif command == "add":
        lst.insert(index, value) if index == 0 else lst.append(value)
        return lst

# remove
lst = [1, 2, 3]
print(list_manipulation(lst, 'remove', 'end'), 3)
print(list_manipulation(lst, 'remove', 'beginning'), 1)
print(lst, [2])

# add
lst = [1, 2, 3]
print(list_manipulation(lst, 'add', 'beginning', 20), [20, 1, 2, 3])
print(list_manipulation(lst, 'add', 'end', 30), [20, 1, 2, 3, 30])
print(lst, [20, 1, 2, 3, 30])

# invalid
print(list_manipulation(lst, 'foo', 'end') is None, True)
print(list_manipulation(lst, 'add', 'dunno') is None, True)