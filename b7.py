#7. Write a function that makes a list with unique items from a list with duplicate items. Example: [1, 1, 2, 3, 3] -> [1, 2, 3]
def unique_items(list_items):
    list_unique_items = set(list_items)
    return list_unique_items

if __name__ == '__main__':
    list1 = [1, 1, 2, 3, 3]
    lst_unique = unique_items(list1)
    print(lst_unique)