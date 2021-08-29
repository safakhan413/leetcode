# ## Completing all curated questions
# # https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-75-LeetCode-Questions-to-Save-Your-Time-OaM1orEU
#
def getSum( x,y):
#     '''Algo:
#     Output: sum of two ints without using + or -
#     Input: two ints a and b
#     Step1:
#     Use bitwise manipulation
#     '''
    while (y != 0):
        # carry now contains common
        # set bits of x and y
        carry = x & y
        print(x,y, carry)

        # Sum of bits of x and y where at
        # least one of the bits is not set
        x = x ^ y
        print("im xor operation of x",x)
        # Carry is shifted by one so that
        # adding it to x gives the required sum
        y = carry << 1
        print("im carry shift left", y)

    return x



#     num = int(bin(a))
#     # print(a|b)
#     # print(a^b)
#     # add_aNb = a|b
#     # aNb = a&b
#     # sum = add_aNb | aNb
#     # print(add_aNb, aNb, sum)
#     # | operator gives a+b - (a and b)
#     # so to add you have to add back (a and b)
#
#     # print(a or b)
#
a = 1
b = 1
x = getSum(a,b)
print(x)

# Examples of Bitwise operators
# a = 10
# b = 4
#
# # Print bitwise AND operation
# print(a & b)
#
# # Print bitwise OR operation
# print(a | b)
#
# # Print bitwise NOT operation
# print(~b)
#
# # print bitwise XOR operation
# print(a ^ b)
#
# # print bitwise right shift operation
# print(a >> 2)
#
# # print bitwise left shift operation
# print(a << 2)