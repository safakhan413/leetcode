def myAtoi(s):
    # print('hellloooooooo')
    # x = filter(lambda i: i.isdigit(), s)
    # print('hello', x)
    ## checking sign


    # dig = ''.join(filter(str.isdigit, s))
    # # pos = s.find('-')
    # newS = ''
    # if '-' in s and s[s.find('-')+1].isdigit():
    #     newS = "-"+dig
    #     print(newS)
    #     return int(newS)
    # else:
    #     return int(newS)
    dig = ''.join(filter(str.isdigit, s))
    pos = s.find('-')
    # print(pos)
    if pos >0 and s[pos+1].isdigit():
        dig = "-"+dig
        return int(dig)
    else:
        return int(dig)

    # dig = ''.join(filter(lambda i: i.isdigit(), s))
    # print(dig)
    # for i in dig:
    #     print(i)

s = "42"
print(myAtoi(s))