# check if number entered is a prime number
# from math import sqrt
#
# num = int(input("Enter a number "))
# square = round(sqrt(num))+1
# square = int(square)
# print(f"{square} square")
# i = 2
#
# for i in range(2,square):
#     if num % i == 0:
#         print(f"{num} is not a prime number")
#         break
#     else:
#         print(f"{num} is a prime number")
#         break

# display as many prime numbers as asked
from math import sqrt

# print(f"{square} square")
chosen_number = int(input("Enter how many prime numbers you wish to display "))

n = 1  # how many prime number have been found
prime_list = [1]  # prime number list
check = 2  # number we are checking

while n < chosen_number:
    square = round(sqrt(check)) + 1
    square = int(square)  # square root of the number we are checking
    for i in range(2, square):
        print(i)
        if n % i == 0:
            check = check + 1
            print(check)
        else:
            prime_list.append(check)
            n = n + 1
            print(n)

print(f"Prime list: {prime_list}")
