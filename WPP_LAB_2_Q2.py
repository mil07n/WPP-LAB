dict_items = {}
num = int(input("Enter No. of products needed in dictionary: "))
for i in range(num):
    key = input("Enter product name: ")
    value = int(input("Enter price of product: "))
    dict_items[key] = value
print("\nDictionary of Products and Prices:", dict_items)
print("\nFrom list, choose a product name to get it's price:")
choice = input("Enter product name: ")
print("Press 1 to find price or press 0 to end search")
loop_choice = int(input("Enter the option here: "))
while loop_choice == 1:
    if choice in dict_items:
        print(f"The price of {choice} is: {dict_items[choice]}")
    else:
        print("Product not found, Please try again")
    loop_choice = int(input("\nPress 1 to search again or 0 to end search: "))
    if loop_choice == 1:
        choice = input("Enter product name: ")
print("Search ended.")