# 11382번
# numbers = input().split()
# num1 = int(numbers[0])
# num2 = int(numbers[1])
# num3 = int(numbers[2])
# print(num1 + num2 + num3)


# 25314번
# n = int(input())
# answer = 'int'
# for i in range(n//4):
#     answer = 'long ' + answer
# print(answer)


# 27866번
# word = input()
# number = int(input())
# print(word[number-1])


# 2743번
# word = input()
# print(len(word))


# 9086번
# number = int(input())
# word_list = [input() for _ in range(number)]

# for word in word_list:
#     if len(word) == 1:
#         print(word+word)
#     else:
#         print(word[0]+word[-1])


# 1152번
# temp_str = input()
# print(len(temp_str.split()))


# 1718번
# while True:
#     try:
#         print(input())
#     except EOFError:
#         break


# 2444번
# num = int(input())
# length = (2 * num) - 1
# star_num = 1
# blank_num = num - 1

# for i in range(1, length+1):
#     blank = ' ' * blank_num
#     star = '*' * star_num
#     print(blank + star)
#     if i < num:
#         star_num += 2
#         blank_num -= 1
#     else:
#         star_num -= 2
#         blank_num += 1


# num = int(input())

# for i in range(1, 2 * num):
#     star_num = 2 * (num - abs(num - i)) - 1
#     blank_num = abs(num - i)
#     print(' ' * blank_num + '*' * star_num)


# 10988번
# temp_str = input()

# 2941번
# croatia_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# result = 0

# 1157번
# text = input().lower()

# temp_dict = {}

# max_text = ''
# max_count = 0

# for item in text:
#     if item in temp_dict.keys():
#         temp_dict[item] += 1
#     else:
#         temp_dict[item] = 1

# for key, value in temp_dict.items():
#     if value > max_count:
#         max_text = key
#         max_count = value
#         is_duplicate = False
#     elif value == max_count and max_count != 0:
#         is_duplicate = True
        
# if is_duplicate:
#     print('?')
# else:
    # print(max_text.upper())
    

# 1157번 수정본
from collections import Counter

text = input().upper()
counter = Counter(text)

max_count = max([value for value in counter.values()])
max_char = [key for key, value in counter.items() if value == max_count]

if len(max_char) > 1:
    print('?')
else:
    print(max_char[0])