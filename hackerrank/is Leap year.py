def is_leap(year):
    leap = False
    if year%4 ==0 and (year%400 == 0 or year%100 !=0):
        return True

    # Write your logic here

    return leap

year = 2400
print(is_leap(year))

'''Algorithm
Output: voolean valeu true if leap year otherwise false
input: year

step1. What conditiosn are true divisible by 4 yes, another nested if condition 
'''