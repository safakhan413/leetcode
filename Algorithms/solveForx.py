
import cmath
import logging


a = 0
b = 1.0
c = 1.0
done = False
x = cmath.inf
print('value of x is {}'.format(x))
# while not done:
#     # a = 0
#     # b = 1.0
#     # c = 1.0
#     a = float(input('a = '))
#     b = float(input('b = '))
#     c = float(input('c = '))
#     if a == 0:
#         logging.warning("we are sorry. A can't be 0. Please try again!")
#         continue
#     try:
#         root = cmath.sqrt(b * b - 4.0 * a * c)
#         x1 = (-b + root) / (2.0 * a)
#         x2 = (-b - root) / (2.0 * a)
#         print(x1)
#         print(x2)
#         done = True
#     except ZeroDivisionError as error:
#         logging.error(error)
#         print('a can not be 0. please try again')
