shopping_list = ['apples', 'banana', 'milk']
# Start with shopping_list = ['apples', 'bananas', 'milk']

# 1. Append 'bread' to the list
shopping_list.append("bread")
print("After adding 'bread' to the list", shopping_list)

# 2. Insert 'eggs' at position 1
shopping_list.insert(1, 'eggs')
print("After inserting 'eggs' in index 1", shopping_list)

# 3. Remove 'bananas'
shopping_list.remove('banana')
print("After removing 'banana' from the list:", shopping_list)

# 4. Sort the list alphabetically
shopping_list.sort()
print("After sorting the list", shopping_list)

# 5. Reverse the list
shopping_list.reverse()
print("Reversed list", shopping_list)

# 6. Create a new list with the first 3 items
new_shopping_list = list(shopping_list[:3])
print("New Shopping list:", new_shopping_list)

# 7. Print the length of the list
print("The length of old shopping list is", len(shopping_list))
print("And the length of new one is:", len(new_shopping_list))