def common_items(list1, list2):
    common_items_count = 0
    for item in list1:
        if item in list2:
            common_items_count += 1
    return common_items_count

def main():
    # Accepting lists from the user
    list1 = []
    list2 = []

    print("Enter 5 unique items for the first list:")
    for i in range(5):
        item = input("Item {}: ".format(i+1))
        list1.append(item)

    print("Enter 5 unique items for the second list:")
    for i in range(5):
        item = input("Item {}: ".format(i+1))
        list2.append(item)

    # Finding common items
    common_count = common_items(list1, list2)
    print("Number of common items:", common_count)

if name== "main":main()
