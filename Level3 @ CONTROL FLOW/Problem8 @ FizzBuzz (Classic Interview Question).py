# # Print numbers from 1 to 50
onetofifty = []
for i in range(51):
    onetofifty.append(i)
print("One to Fifty with for loop:", onetofifty)

# With while loop
whileonetofifty = []
i = 1
while i <= 50:
    whileonetofifty.append(i)
    i += 1
print("\nOne to Fifty with while loop:", whileonetofifty)

# For multiples of 3, print "Fizz" instead of the number
print("\n I'm writing Fizz instead of Numbers whis are multiples of 3:")
list = []
for i in range(51):
    if i % 3 == 0:
        i = "Fizz"
    list.append(i)
print(list)

# For multiples of 5, print "Buzz" instead of the number
buzz5 = []
for i in range(51):
    if i % 5 == 0:
        i = "Buzz"
    buzz5.append(i) 
print("\nReplaced the numbers which are multiples of 5 to 'Buzz'", buzz5)

# For multiples of both 3 and 5, print "FizzBuzz"
fizzbuzz = []
for i in range(51):
    if i % 3 & 5 == 0:
        i = "FizzBuzz"
    fizzbuzz.append(i)

print("\n Replaced the multiples of 3 and 5 to 'FizzBuzz'", fizzbuzz)