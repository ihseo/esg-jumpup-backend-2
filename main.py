
# student_list = ["a", "b", "c"]
# studentList = [1, 2, 3,]


# 공간에 데이터를 저장하는 것

# a = 10
# b = 5
# c = 2.5
# d = "5"
# is_success = True
# is_late = False
# name = "서인혁"  # 문자열, string

# 문자열, 정수, 소수, Boolean (참/거짓을 뜻할 수 있는 데이터 타입)
# print(13 % 3)
# print(2 ** 3)
# float , str
# str, mul
# import math
# print(math.ceil(5.5))

# print("문자열이다" * 10)



a = 5
b = 3.0
c = "hello"  # 'hello'

# memory
# print(a)
# print("\"hello\"")

960 # h
964 # e
968 # l 
972 # l
976 # o

a = "hello"  # 0, 1, 2, 3, 4
# print(len(a))
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])


# h e l l o


# my_list = [1, 2, 3, 4, "hello"]
# a = "Dog is love"
# print(a[7:])
# print(a[7:11])
# print(a[7:len(a)])
# print(a[-4:])


# a = "010-2244-1234"
# print(a.replace("-", ""))

# a = "hello"
# b = "python"
# print(a + "!" + b)


# my_list = [1, 4, 3, 2, 5]
# print(sorted(my_list))

# my_list = ["a", "c", "e", "d"]
# my_list.reverse()
# print(my_list)



# key, value (이름, 값)
# my_dictionary = {
#     # "name": "Ian Seo",
#     "age": 34,
#     "office_location": "dangsan",
#     "favorite_foods": [
#         "pizza", "hamburger"
#     ]
# }

# print(my_dictionary["name"])
# print(my_dictionary.get("name", "unknown"))

# score_dictionary = {
#     "A": 90,
#     "B": 80,
#     "C": 70,
#     "D": 60
# }

# print(score_dictionary.get("Bb", "Bad input"))

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# print(set1 & set2)
# print(set1.intersection(set2))

# print(set1 - set2)
# print(set1 | set2)  # 합집합

# print(5 == 5)  # True / False 가 나옵니다
# print(5 > 3)
# print(3 > 5)
# print(3 <= 5)

# score = int(input("Enter score: "))
# if 0 <= score <= 100:
#     if 90 <= score <= 100:
#         print('A')
#     elif 80 <= score < 90:
#         print('B')
# elif 80 <= score < 90:
#     print('C')

# 점수를 input 으로 받아서 A, B, C, D, F 를 주는 코드를 만들어보세요



# 4
# int(4/2) == 2
# int(5/2) == 2
def say_my_name(name="John"):
    print("Hello", name)

def add(num1, num2):
    answer = num1 + num2
    return answer

# say_my_name("Ian")
# say_my_name("Rachael")
# say_my_name()

import time
import random

# print(random.randint(0, 10))


# 숫자 하나를 function이 입력받아서
# 만약 5라면
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 9 = 45

# def multiply_box():
#     number = int(input("Enter a number between 2 to 9: "))
#     for i in range(1, 10):
#         print(number, "x", i, "=", number * i)

# multiply_box()

# print(5 > 3)
# print(20 == "20")
# print(10 >= 2)

# print(2 < 3 or 5 < 3)  # True
# print(not 2 < 3)

# i = 0
# while i < 5:
#     print('i value is', i)
#     i += 1  # i = i + 1

# print('i value: ', i)

# range(5)  # 0, 1, 2, 3, 4
# for i in range(5, 0, -1):
#     print(i)

fruits = ["banana", "strawberry", "blueberry"]
# for kid in the group

# for fruit in fruits:
#     print(fruit)

# for i in range(len(fruits)):
#     print(fruits[i])

# def multiply_box(num):
#     # 1단부터 9단까지
#     for i in range(1, 10):
#         print(num, 'x', i, '=', num * i)

# multiply_box(5)


# foods_list = ["pizza", "hamburger", "chicken", "salad"]

# for i, food in enumerate(foods_list):
#     print(i)

def coffee_vending_machine():
    # dictionary를 써서 어떤 메뉴들을 만들어놓고
    # 거기에 대한 입력을 받게 하고
    # 메뉴가 있는지 체크해야 하고
    # 돈을 받는다.
    # 금액이 모자란지 체크를 하고, 거스름돈을 준다.
    coffee_options = {
        '1': {'name': 'Americano Ice', 'price': 2000},
        '2': {'name': 'Americano Hot', 'price': 1500},
        '3': {'name': 'Vanilla Latte Ice', 'price': 2500},
        '4': {'name': 'Earl Grey Tea Vanilla Latte Ice', 'price': 5800}
    }

    print('Welcome! here\'s the menu')
    for key, value in coffee_options.items():
        print(key, ':', value)
    
    choice = input("Please select menu : ")
    # if choice not in coffee_options:
        # print('invalid menu')
        # return
    while (choice not in coffee_options):
        print('invalid menu, choose again')
        choice = input("Please select menu : ")
    
    amount_paid = int(input("액수를 입력해주세요 : "))
    price = coffee_options[choice].get('price')

    if amount_paid == price:
        print(f'thank you! enjoy your {coffee_options[choice]["name"]}')
    elif amount_paid > price:
        change = amount_paid - price
        print('thank you! change : ', change)
    else:
        print('Insufficient amount')
    


    # 기획 # 경우의 수

# coffee_vending_machine()

# a = 500
# import random
# print(f'{a} 입니다 {random.randrange(0, 10)}')  # format string
# print(a, '입니다')




fruits = ["banana", "strawberry", "blueberry", "apple", "orange", "grape"]
# loop through the list
for fruit in fruits:
    print(fruit)

