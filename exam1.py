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

# solution if 8
# print(" solution if 8")
# num: int = int(input("Enter number :"))
# ahadot: int
# asarot: int
#
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












