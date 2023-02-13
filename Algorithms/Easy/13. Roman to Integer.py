def romanToInt(s):
    # print(s)
    roman_to_integer = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        '0':0
    }
    '''
    Algo:
    output: int values
    input: roman values 
    steps:
    1. create a dict for mapping
    2. in for loop track both pres and next value. 
    Cases:
    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
    if presentvalues is V or X check prev value is I, if I then minus, otherwise add to final string


    '''
    # for char in s:
  
    intVal = 0
    for i in range(len(s)):
        if i+1 < len(s) and roman_to_integer[s[i]] < roman_to_integer[s[i+1]]:
            intVal -= roman_to_integer[s[i]]
        else:
            intVal += roman_to_integer[s[i]]

    return intVal


s = "MCMXCIV"
print(romanToInt(s))