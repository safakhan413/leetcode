# #not an interview question but a practice one
# Q3: Write a program that will find all such numbers which are divisible by 7 but are 
# not a multiple of 5, between 2000 and 2100 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def divby7Notmulti5():
    x=''
    y = []
    for i in range(2000,2101):
        if i%7 == 0 and i%5 !=0:
            # x= ",".join(i)
            y.append(str(i))
    x= ','.join(y)
    print(x)
divby7Notmulti5()