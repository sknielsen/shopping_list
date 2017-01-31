shopping_list = []

def add_item(item, list):
    if item.lower() in list:
        print "%s is already in the list." % (item)
    else:
        list.append(item.lower())
        return a_to_z(list)

def a_to_z(list):
    return list.sort()

def remove_item(item, list):
    if item.lower() not in list:
        print "%s doesn't exist" % (item)
    else:
        list.remove(item.lower())
        return a_to_z(list)

def main():
    add_item("Apples", shopping_list)
    add_item("pears", shopping_list)
    add_item("Oranges", shopping_list)
    add_item("bananas", shopping_list)
    add_item("pears", shopping_list)
    remove_item("pears", shopping_list)
    remove_item("Grapes", shopping_list)
    print shopping_list

if __name__ == '__main__':
    main()
#shopping_list = ['apples', 'pears', 'oranges']
#add_item('Apples', shopping_list)
#remove_item('pears', shopping_list)
#print shopping_list