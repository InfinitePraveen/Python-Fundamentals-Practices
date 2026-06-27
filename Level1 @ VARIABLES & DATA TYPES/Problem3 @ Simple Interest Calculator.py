# Simple Interest = (Principal * Rate * Time) / 100

principal = int(input("Enter your principal amount: "))
rate = int(input("Enter your rate of interest: "))
time = int(input("Now, Enter the time/year: "))

# Principal = 1000
# Rate = 5.5
# Time = 3 years

# Calculate and print the interest and total amount
interest = (principal * rate * time) / 100

# Print Statement
print(f"Your interest is {interest} and your total amount is {interest+principal}")