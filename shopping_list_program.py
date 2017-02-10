shopping_list = { "Target": ["socks" , "soap", "detergent", "sponges"],
"Bi-Rite" : [ "butter", "cake", "cookies", "bread"] }

#Function to display main Menu
def show_main_menu():
    return """ 
0 - Main Menu
1 - Show all lists.
2 - Show a specific list.
3 - Add a new shopping list.
4 - Add an item to a shopping list.
5 - Remove an item from a shopping list.
6 - Remove a list by nickname.
7 - Exit when you are done.
"""

#Function that shows all lists
def show_all_lists():
    # print shopping_list
    for nickname in shopping_list:
        print nickname + ': ' + ", ".join(shopping_list[nickname])
    #for nickname in shopping.list:


#Function to show a specific list
def show_specific_list(list):
    print list + ': ' + ", ".join(shopping_list[list])

#
def add_new_list(item, list):
    shopping_list[list] = item


def add_item_to_list(item, list):
    shopping_list[list].append(item)
    return shopping_list


def remove_item_from_list(item, list):
    shopping_list[list].remove(item)
    return shopping_list


def remove_list(list):
    del shopping_list[list]
    return shopping_list


def exit_program():
    exit()




def main():
    #show_main_menu()

    user_input = int(raw_input(show_main_menu()))
    if user_input == 0:
        print show_main_menu()
    elif user_input== 1:
        show_all_lists()
    elif user_input == 2:
        list = raw_input("Enter list to be displayed")
        show_specific_list(list)
    elif user_input == 3:
        list = raw_input("Enter new list name")
        item = raw_input("Enter items for new list")
    #show_main_menu()
    #show_all_lists()
    #show_specific_list('Target')
    #print add_item_to_list('brush', 'Target')
    #print remove_item_from_list('soap', 'Target')
    #print remove_list('Target')

if __name__ == '__main__':
    main()
