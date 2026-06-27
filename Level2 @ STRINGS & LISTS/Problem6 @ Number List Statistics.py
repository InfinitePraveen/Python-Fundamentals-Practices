numbers = [12, 7, 19, 24, 5, 31, 8, 16]

# 1. Find and print the largest number
largest_number = max(numbers)
index_largest_number = numbers.index(largest_number)
print("The largest number in the list is", largest_number, "and his index is", index_largest_number)

# 2. Find and print the smallest number
smallest_number = min(numbers)
index_smallest_number = numbers.index(smallest_number)
print("The smallest number is", smallest_number, "and his index is", index_smallest_number)

# 3. Calculate and print the sum
print("The sum of all numbers in the list is", sum(numbers))

# 4. Calculate and print the average
average = sum(numbers)/(len(numbers)+1)
print("The Average of sample list is", average)

# 5. Count numbers greater than 15
greater_than15 = [num for num in numbers if num > 15]
print("The number of values in the list that are greater than 15 are", greater_than15)

# 6. Create a new list of even numbers only
even_numbers = [even for even in numbers if even % 2 == 0]
print("New list of even numbers:", even_numbers)