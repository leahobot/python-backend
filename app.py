
import code
import random
import secrets
from statistics import mean, variance
import math
# def prime_number(number: int):
#     if number > 1:
#         for item in range(2, number):
#             if(number % item == 0):
#                 return False
#                 break
#         return True
#     return False


# print(prime_number(4))

# print("Guess the computer's choice to win the prize.")

# a = [1, 2, 3, 4, 5, 6, 7]
# random.shuffle(a)

# trial = 3
# score = 0

# while trial > 0:
#     print("Select a number from", a)
#     com_choice = random.choice(a)
#     user = int(input("Your choice: "))
#     if user == com_choice:
#         print("You win")
#         score += 2
#         trial += 1
#         print("You have won an extra trial")
#         print(f"{trial} trial(s) left")

#     else:
#         if user > com_choice:
#             print("Too high")
#         else:
#             print("Too low")
#         trial -= 1
#         print(f"{trial} trial(s) left")
# print(f"You scored {score} points")
# print("Game Over")


# options = ["r", "p", "s"]
# trial = 3
# score = 0

# while trial > 0:
#     print("""
#           Select R for rock, P for paper and S for scissors.
#           """)
#     com_choice = random.choice(options)
#     player_choice = input(">").lower()
#     if player_choice == options[0] and com_choice == options[2]:
#         print("You win")
#         print("Computer choose", com_choice)
#         trial += 1
#         score += 2
#     elif player_choice == options[2] and com_choice == options[1]:
#         print("You win")
#         print("Computer choose", com_choice)
#         trial += 1
#         score += 2
#     elif player_choice == options[1] and com_choice == [0]:
#         print("You win")
#         print("Computer choose", com_choice)
#         trial += 1
#         score += 2
#     elif player_choice == com_choice:
#         print("It's a tie")
#     else:
#         print("You lose")
#         print("Computer choose", com_choice.title())
#         trial -= 1
# else:
#     print("Invalid output")
#     trial -= 1
#     print(f"{trial} trial(s) left")

# print("Game Over")
# print("You scored", score)a

# def prime_number(number: int):
#     if number > 1:
#         for item in range(2, number):
#             if(number % item == 0):
#                 return False
#                 break
#         return True
#     return False


# a = [x for x in range(98, 176) if prime_number(x)]

# print(a)


# sentence = "This is a common interview question"

# common = {}
# for item in sentence:
#     if item in common:
#         common[item] += 1
#     else:
#         common[item] = 1

# sorted_word = sorted(common.items(), key=lambda item: item[1], reverse=True)
# print(sorted_word[0])


# 1. Mean

# def mean(*numbers):
#     return sum(numbers)/len(numbers)


# print(mean(2, 3, 4, 5, 5, 5, 55, 5))


# 2. Median

# def median(*numbers: int):
#     length = len(numbers)
#     sorted_numbers = sorted(numbers)
#     if length % 2 == 0:
#         even_one = sorted_numbers[length//2]
#         even_two = sorted_numbers[length//2 - 1]
#         return (even_one + even_two) / 2
#     else:
#         odd_length = (length//2)
#         return sorted_numbers[odd_length]


# print(median(10, 11, 18, 26, 45, 55, 89, 89, 90, 63))


# 3. variance

# def variance(*numbers):
#     length = len(numbers)
#     mean = sum(numbers)/length
#     deviation = [(x - mean) ** 2 for x in numbers]
#     variance = sum(deviation) / (length - 1)
#     return variance


# print(round(variance(2, 4, 5), 2))


# 4. Standard Deviation

# def stan_dev(*numbers):
#     length = len(numbers)
#     mean = sum(numbers)/length
#     deviation = [(x - mean) ** 2 for x in numbers]
#     variance = sum(deviation) / (length - 1)
#     standard_deviation = math.sqrt(variance)
#     return standard_deviation


# print(round(stan_dev(2, 4, 5), 2))


# # 5. Skewness

# def skewness(*numbers):
#     length = len(numbers)
#     mean = sum(numbers)/length
#     deviation = [(x - mean) ** 2 for x in numbers]
#     variance = sum(deviation) / (length - 1)
#     standard_deviation = math.sqrt(variance)
#     return standard_deviation


# print(round(skewness(2, 4, 5), 2))


# a = [1, 2, 4, 7, [5, 9, [8, 7], 4], 3, 7]

# b = a[4][1] + a[4][2][0]

# print(b)

# a = [4, 3, 2, 1, 8]

# b = a.copy

# b[3] = 7

# print(b)
# print(a)

# a = ["mike", "", "emma", "", "kelly", "", "brad"]


# print(a[0:7:2])

import random
import string


# def otp(x):
#     generate = []
#     for a in range(x):
#         generate.append(str(random.choice(range(10))))
#         generate.append(random.choice(string.ascii_letters))
#         random.shuffle(generate)
#     return "".join(generate)


# class Point:
#     def draw(self):
#         print("draw")


# print(Point.draw(2))

# a = {3, 4, 7, 8, 10, 17}
# b = {2, 4, 6, 8, 10, 12}
# c = a - b


# first = {1, 2, 3, 8, 10}
# second = {4, 5, 6, 17, 12}
# third = first.symmetric_difference_(second)
# print(third)

# english = input("Enter total number of English students >:")
# english_newspaper = set(input("Enter the roll numbers >:").split())

# french = input("Enter total number of French students >:")
# french_newspaper = set(input("Enter the roll numbers >:").split())

# total = english_newspaper ^ french_newspaper

# print(f"The total subscribed to either of both is {len(total)}")

# a = {"a": 1, "b": 2, "c": 3, "d": 4}

# print(a["d"])

# for item in sentence:
#     #     if item in common:
#     #         common[item] += 1
#     #     else:
#     #         common[item] = 1

# a = [random.choice(range(10)) for i in range(1000)]

# b = {}

# for item in set(a):
#     b[item] = a.count(item)

# print(b)


# for item in a:
#       b[item] = b(item, 0) + 1

# print(b)
