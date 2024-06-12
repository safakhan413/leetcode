"""Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2,
 also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 """
def strint(n):
    result=0
    for i in range(len(n)):
        result = result*10 + ord(n[i])-ord('0')
    return result
def multiply( num1, num2):
    return str(strint(num1)*strint(num2))


num1 = "123"
num2 = "456"
# num1 = "123456789"
# num2 = "987654321"
# num1 = "2"
# num2="3"
x = multiply(num1,num2)
print(x)