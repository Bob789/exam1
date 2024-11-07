# solution if 1
# print(" solution if 1")
# num1: float = float(input("Enter num1: "))
# num2: float = float(input("Enter num2: "))
# smaller: float = 0
# if num1 < num2:
#     smaller = num1
# else:
#     smaller = num2
#
# print(f" smaller {smaller}")
# print(f" smaller {smaller}")
# print(f" smaller {smaller}")
from operator import index
from random import random
from sys import flags

# solution if 2
# print(" solution if 2")
# shalem1: int = int(input("Enter num1: "))
# shalem2: int = int(input("Enter num2: "))
# avr: float = (shalem1 + shalem2)/2
# print(f" Avrage: {avr}")

# solution if 3
# print(" solution if 3")
# num1: int = int(input("Enter number"))
# num2: int = int(input("Enter number"))
# num3: int = int(input("Enter number"))
# bignumber: int = 0
# if num1 > num2:
#     bignumber = num1
# else:
#     bignumber = num2
# if bignumber > num3:
#     print(f" The big number is: {bignumber}")
# else:
#     print(f" The big number is: {num3}")

# solution if 4
# print(" solution if 4")
# movie_time_min: int = int(input("Enter length of the movie in minutes :"))
# houer: int = int(movie_time_min / 60)
# minute: int = movie_time_min % 60
# print(f"houer : {houer}  minute : {minute}" )

# solution if 5
# print(" solution if 5")
# while True:
#     numbers: str = str(input("Enter number 4 digit: "))
#     if len(numbers) == 4:
#         if numbers.isdigit():
#             print("The last digit are :", numbers[-1])
#             break

# solution if 6
# print(" solution if 6")
# while True:
#     numbers: str = str(input("Enter number 4 digit: "))
#     if len(numbers) == 4:
#         if numbers.isdigit():
#             print("The second digit from the end are :", numbers[-2])
#             break

# solution if 7
# print(" solution if 7")
# num: int = int(input("Enter number :"))
# print(num)
#
# ahadot = num % 10
# asarot = num // 10
# print(f" The sum fo {asarot} + {ahadot} = {ahadot + asarot}")

# solution if 8
# print(" solution if 8")
# num: int = int(input("Enter number :"))

# print(num)
# ahadot = num % 10
# print(ahadot)
# asarot = num // 10
# print(asarot)
# print(f" The reverse number : {(ahadot * 10) + asarot}")

# solution if 9
# print(" solution if 9")
# num: int = int(input("Enter number :"))
# if num % 2 == 0:
#     print(f"Even {num}:")
# else:
#     print(f"Odd {num}")


# solution if 10
print(" solution if 10")
salary = int(input("Enter a salary: "))
tax: float = 0
if salary <= 6000:
    print(f"for {salary} you pay tax {tax}")
if 6000 < salary:
    if salary < 12001:
        tax = (salary - 6000) * 0.1
    else:
        tax = (12000 - 6000) * 0.1
if 12000 < salary:
    if salary < 18001:
        tax = tax + (salary - 12000) * 0.2
    else:
        tax = tax + (18000 - 12000) * 0.2
if 18000 < salary:
    if salary < 25001:
        tax = tax + (salary - 18000) * 0.3
    else:
        tax = tax + (25000 - 18000) * 0.3
if 25000 < salary:
    if salary < 35001:
        tax = tax + (salary - 25000) * 0.4
    else:
        tax = tax +(35000 - 25000) * 0.4
if 35000 < salary:
    if salary < 50001:
        tax = tax + (salary - 35000) * 0.45
    else:
        tax = tax + (50000 - 35000) * 0.45
if salary > 50000:
    tax = tax + (salary - 50000) * 0.51



print(f" Total tax for your {salary} are : {tax}")

# solution if 11
# print(" solution if 11")
# age = float(input("Enter a age: "))
# height = float(input("Enter a height: "))
#
# if 8 <= age <= 18 and 115 <= height:
#     print("You may allow to enter roller coaster")
# elif 18 < age and 100 < height:
#     print(print("You may allow to enter roller coaster"))
# else:
#     print("You are not allow to enter roller coaster")

# -----------------------------------------------------------------------------------

# solution loop 1
# print("solution loop 1")
# num: int = int(input("Enter number: "))
#
# for x in range(1, num+1):
#     print(x)

# solution loop 2
# print("solution loop 2")
# num1: int = int(input("Enter number"))
# num2: int = int(input("Enter number"))
# start: int
# end: int
#
# if num1 < num2:
#     start = num1
#     end = num2
# else:
#     start = num2
#     end = num1
# for start in range(start, end):
#     if start % 2 == 0:
#         print(start)

# solution loop 3
# print("solution loop 3")
# end: int = int(input("Enter number :"))
#
# for start in range(end):
#     if start % 2 == 0:
#         print(start)

# solution loop 4
# print("solution loop 4")
# maxx: int = int(input("Enter number max:"))
# den: int = int(input("Enter number den:"))
#
# for start in range(den, maxx+1):
#     if start % den == 0:
#         print(start)

# ----------------------------------------------------------------------------------------
#process data 1
# print(" Process data: 1")
# SENTIENEL: int = -99
# numbersum: int = 0
# inputnumber: int = int(input("Enter number :"))
# if inputnumber == SENTIENEL:
#     print("None")
# while True:
#
#     if SENTIENEL != inputnumber:
#         numbersum += inputnumber
#         inputnumber = int(input("Enter number :"))
#     else:
#         break
#
# print(f"The sum of input number : {numbersum}")

#process data 2
# print(" Process data: 2")
# SENTIENEL: int = 0
# inputnum: int
# inputnumbers: list [int] = []
# while True:
#     inputnum: int = int(input("Enter number :"))
#     if inputnum <= SENTIENEL:
#         break
#     else:
#             inputnumbers.append(inputnum)
#
# print(f"The biggest number are: {max(inputnumbers)}")
# print(f"The smallest number are: {min(inputnumbers)}")

#process data 3
# print(" Process data: 3")
# num: list[int] = []
# for x in range(5):
#     num.append(int(input("Enter number: ")))
#
# print(f"The index of {max(num)}  are {num.index(max(num))+1}")

#process data 4
# print(" Process data: 4")
# numa: int = int(input("Enter number :"))
# numb: int = int(input("Enter number :"))
# count: int = numa
# numab: int = 0
#
# while  count !=0:
#     numab += numb
#     count -= 1
#
# print(f" {numa} * {numb} = {numab}")

#process data 5
# print(" Process data: 5")
# base: int = int(input("Enter number1 :"))
# exponent: int = int(input("Enter number2 :"))
# power: int = base
# count = exponent
# while count > 1:
#     power *= base
#     count -=1
#
# print(F" The Power are :{power}")

#process data 6
# print(" Process data: 6")
# number: str = str(input("enter number :"))
# digit: str = str(input("enter digit :"))
#
# if digit in number:
#     print(True)
# else:
#     print(False)

#process data 7
# print(" Process data: 7")
# num1: int = int(input(" Enter number 1:"))
# num2: int = int(input(" Enter number 1:"))
# big_number_devided: int = 0
#
# list_d = [i for i in range(1, int(num1) + 1) if num1 % i == 0]
# list_e = [i for i in range(1, int(num2) + 1) if num2 % i == 0]
#
# for i in list_d:
#     if i in list_e:
#         big_number_devided = i
#
# print(f" The big number devided :{big_number_devided}")

#process data 8
# print(" Process data: 8")
# x: int = int(input("Enter number to check is prime number :"))
# if x > 1 and not any(x % i == 0 for i in range(2, int(x ** 0.5) + 1)):
#     print(f"{x} is a prime number ")
# else:
#     print(f"{x} is not a prime number ")


#----------------------------------------------------------------------------------------
# complex loops 1
# from statistics import mean
# print("complex loops 1")
# list_temperature: list[float] = []
# temp: float
# cards12: int = 3
#
# for index in range (1,cards12 + 1):
#     while True:
#         try:
#             temp = float(input(f"Enter temperature card {index}: "))
#             break
#         except ValueError:
#             print("The input is not a number.")
#
#     if -5 <= temp <= 40:
#         list_temperature.append(temp)
#     else:
#         print("Wrong data")
#         break
# #   end while
# if len(list_temperature) == cards12:
#     print("Correct data")
#     average = mean(list_temperature)
#     print("Average temperature of the 2023:", average)
#     print(f" The max temperature are: {max(list_temperature)}")
#     print(f" The min temperature are: {min(list_temperature)}")
#
# print(list_temperature)

# complex loops 2
# print("complex loops 2")
# list_states_vote: list[int] = []
# end: int = 44
# list_number_vote: list[int] = [1, 2, 3, 4]
# option_vote: list[str] = ["favor", "against", "avoided", "veto"]
#
# topic: str = input("What is the topic issue to vote on: ")
# print(f"We are voting on a {topic} issue:")
# flag: bool = False
# for i in range(1, end):
#     if flag:
#         break
#     while True:
#         try:
#             vote = int(input("Enter vote (1 | 2 | 3 | 4): "))
#             if vote in list_number_vote:
#                 list_states_vote.append(vote)  # Add the valid vote to the list
#                 if 4 in list_states_vote:
#                     print(f" country {len(list_states_vote)} vote {option_vote[3]}")
#                     flag = True
#                     break
#                 break
#             else:
#                 print("Invalid choice. Please enter 1, 2, 3, or 4")
#         except ValueError:
#             print("Invalid input. Please enter a number between 1 and 4")
#
# print("Votes collected:", list_states_vote)
# print(f" The first country which vote {option_vote[0]} are {list_states_vote.index(1)+1}")
# print(f" The first country which vote {option_vote[1]} are {list_states_vote.index(2)+1}")











