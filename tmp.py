import calc as cl

print("Сначала вводим действительную и мнимую части первого числа:")
a1, b1 = cl.input_2_num()
print("Теперь действительную и мнимую части второго числа:")
a2, b2 = cl.input_2_num()
print(a1,b1,"\n",  a2,b2)
c1 = complex(float(a1), float(b1))
c2 = complex(float(a2), float(b2))
print(f"Вы ввели комплексные числа {c1} и {c2} ")
print(f"{c1**3}, {c1**0.5}")
# logging.info((f'Input two complex {c1} , {c2}'))

# # a, b = "", ""
# # while not a and not b:
# #     print("ВВедите два числа через пробел: ")
# #     ls = input().split()
# #     # if len(ls) == 2 and ls[0].isnumeric() and ls[1].isnumeric():
# #     if len(ls) == 2 and type (ls[0])== "float" and ls[1].isnumeric():
# #         a, b = ls

# import numbers


# def isint(s):
#     try:
#         float(s) or int(s)
#         return float(s)
#     except ValueError:
#         return False


# def print_result(a):
#     print(f"\033[31m*"*40)
#     print(a)
#     print("*"*40, f"\033[0m")

# print_result(33)

# a= "2"
# print(a.count("-"))
# print(isint(a))
# # print(isint(a))
# print(a.isnumeric())
# # print(f"== {a}, {b} ==")


# variable= 5
# print(isinstance(a, numbers.Number))
