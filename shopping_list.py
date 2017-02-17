'''
Shopping List - now with string parsing
There is a dictionary that contains shopping lists by name.
We'll have a menu with options.
The core logic is in the main() function.

Recommended to review the main() function, and new this week is
parse_input_string()
'''


def add_new_shopping_list(lists_by_name, new_list_name):
    '''
    Given a dictionary that has string keys (shopping list names) add a new
    shopping list key with an empty list as its value.

    Will not allow duplicate shopping list names to be added.  This method
    is case-sensitive

    Argumemts:
      lists_by_name: dict of shopping lists
      new_list_name: string name of the new list to add
    Returns:
      dict: the updated shopping lists dict
    '''
    if new_list_name not in lists_by_name:
        lists_by_name[new_list_name] = []
    else:
        print 'A list named %s already exists!' % new_list_name
    return lists_by_name


def remove_shopping_list(lists_by_name, list_name_to_remove):
    '''
    Given a dictionary that has string keys (shopping list names) remove a
    shopping list from the dictionary if it exists.

    If the shopping list name does not exist in the dictionary, print a message
    and do nothing.  This method is case-sensitive

    Argumemts:
      lists_by_name: dict of shopping lists
      list_name_to_remove: string name of the list to remove
    Returns:
      dict: the updated shopping lists dict
    '''
    if list_name_to_remove in lists_by_name:
        del lists_by_name[list_name_to_remove]
        print 'The %s shopping list has been removed.' % list_name_to_remove
    else:
        print 'There was no list named %s.' % list_name_to_remove


def add_item_to_shopping_list(lists_by_name, list_name, item_name):
    '''
    Given a dictionary of shopping lists, a shopping list name, and an item
    name, add that item to the given shopping list, and print the updated list.

    If the shopping list does not exist, print a message and do nothing.  If
    the item is on the list, print a message and do nothing.  Note that items
    are case insensitive, but list names are case sensitive.

    Arguments:
      lists_by_name: dict of shopping lists
      list_name: string name of a shopping list
      item_name: string name of item to add to the list
    Returns:
      dict: the updated shopping lists dict
    '''
    if list_name in lists_by_name:
        shopping_list = lists_by_name[list_name]

        # make the item name lowercase so we can be case insensitive
        item_name = item_name.lower()

        if item_name not in shopping_list:
            shopping_list.append(item_name)
            print 'Here is your updated list: ', sorted_shopping_list(
                lists_by_name, list_name)
        else:
            print 'This item %s is already on the %s list!' % (
                item_name, list_name)
    else:
        print 'There is no %s list.' % list_name
    return lists_by_name


def remove_item_from_shopping_list(lists_by_name, list_name, item_name):
    '''
    Given a dictionary of shopping lists, a shopping list name, and an item
    name, remove that item from the given shopping list, and print the
    updated list.

    If the shopping list does not exist, print a message and do nothing.  If
    the item is not on the list, print a message and do nothing.  Note that
    items are case insensitive, but list names are case sensitive.

    Arguments:
      lists_by_name: dict of shopping lists
      list_name: string name of a shopping list
      item_name: string name of item to remove from the list
    Returns:
      dict: the updated shopping lists dict
    '''
    if list_name in lists_by_name:
        shopping_list = lists_by_name[list_name]

        # make the item name lowercase so we can be case insensitive
        item_name = item_name.lower()
        if item_name in shopping_list:
            shopping_list.remove(item_name)
            message = ('%s has been removed. Here is your updated list: ' %
                       item_name)
            print message, sorted_shopping_list(lists_by_name, list_name)
        else:
            print '%s was not on the list.' % item_name
            print '  %s has:' % list_name, shopping_list
    else:
        print 'There is no %s list.' % list_name
    return lists_by_name


def sorted_shopping_list(lists_by_name, list_name):
    '''
    Given a dictionary of shopping lists and a shopping list name, sort the
    named list alphabetically and return the sorted list.

    If the list is missing, return a string message saying so.  This method is
    case sensitive

    Arguments:
      lists_by_name: dict of shopping lists
      list_name: string name of a shopping list
    Returns:
      list of strings, sorted alphabetically if the list exists, or a string
        error message if the list does not exist.
    '''
    if list_name in lists_by_name:
        shopping_list = lists_by_name[list_name]
        shopping_list.sort()
        return shopping_list
    else:
        return 'The shopping list %s does not exist' % list_name


def show_all_lists(lists_by_name):
    '''
    Given a dictionary of shopping lists print out the lists.

    Arguments:
      lists_by_name: dict of shopping lists
    Returns:
      None
    '''
    print '\nThe Shopping Lists Are:'
    for shopping_list, list_items in lists_by_name.items():
        print '    %s:' % shopping_list
        for item in list_items:
            print '        %s' % item
    return


def parse_input_string(input_string):
    '''
    Given an input_string split it on commas and return the cleaned up list
    of strings.  Each item in the list has whitespace trimmed.

    Arguments:
      input_string: a string with 0 or more commas separating items
    Returns:
      list of strings.
    '''
    input_string = input_string.strip()
    split_input_list = input_string.split(',')
    items = []
    for item in split_input_list:
        items.append(item.strip())
    return items


def menu_choice():
    '''
    Prints a menu and asks the user to make a choice

    Arguments:
      None
    Returns:
      int: the user's menu choice
    '''
    print '\n    0 - Main Menu'
    print '    1 - Show all lists.'
    print '    2 - Show a specific list.'
    print '    3 - Add a new shopping list.'
    print '    4 - Add item(s) to a shopping list.'
    print '    5 - Remove an item from a shopping list.'
    print '    6 - Remove a list by nickname.'
    print '    7 - Exits the program.\n'

    choice = int(raw_input('Choose from the menu options: '))

    return choice


def write_list_to_file(shopping_list):
    with open('shopping_list.txt', 'w') as shopping_list_file:
        for store in shopping_list:
            shopping_list_file.write('%s: %s\n' %
                                    (store, shopping_list[store]))                                      


def read_file_to_list():
    with open('shopping_list.txt') as shopping_list_file:
        for line in shopping_list_file:
            store, items_string = line.split(':')
            items_string = items.string.replace("['", '')
            items_string = items_string.replace("']", '')
            items_list = items_string.split("', '")
            shopping_lists_by_name[store] = items_list


def main():
    shopping_lists_by_name = {}  # key is list name, value is [shopping list]

    while True:
        choice = menu_choice()

        if choice == 0:
            continue  # continue goes to the next loop iteration

        elif choice == 1:
            show_all_lists(shopping_lists_by_name)

        elif choice == 2:
            list_name = raw_input('Which list would you like to see? ')
            print sorted_shopping_list(shopping_lists_by_name, list_name)

        elif choice == 3:
            list_name = raw_input('Enter the name for your list: ')
            add_new_shopping_list(shopping_lists_by_name, list_name)
            input_str = raw_input('Please enter items separated by commas: ')
            items = parse_input_string(input_str)
            for item in items:
                add_item_to_shopping_list(
                    shopping_lists_by_name, list_name, item)

        elif choice == 4:
            list_name = raw_input('What is the name of the list? ')
            if list_name in shopping_lists_by_name:
                input_str = raw_input(
                    'Please enter items separated by commas: ')
                items = parse_input_string(input_str)
                for item in items:
                    add_item_to_shopping_list(
                        shopping_lists_by_name, list_name, item)
            else:
                print 'There is no %s list.' % list_name

        elif choice == 5:
            list_name = raw_input('What is the name of the list? ')
            if list_name in shopping_lists_by_name:
                input_str = raw_input(
                    'Please enter items to remove separated by commas: ')
                items = parse_input_string(input_str)
                for item in items:
                    remove_item_from_shopping_list(
                        shopping_lists_by_name, list_name, item)
            else:
                print 'There is no %s list.' % list_name

        elif choice == 6:
            list_name = raw_input('What is the name of the list? ')
            remove_shopping_list(shopping_lists_by_name, list_name)

        elif choice == 7:
            break


if __name__ == '__main__':
    main()
