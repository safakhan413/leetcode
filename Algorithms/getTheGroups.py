#!/bin/python3

def getTheGroups(n, queryType, students1, students2):
    # Write your code here
    #n number of students
    print('n:', n)
    print('queryType: ', queryType)
    print('students1: ', students1)
    print('students2: ', students2)
    # make a group when Friend in query
    # return little array
    # if elements common in set AND querytype[j] == friend then they are one group
    # else separate group
    size = len(queryType)
    friends = [0] * size
    for idx, q in enumerate(queryType):
        if (q == 'Friend'):
            # print(idx)
            friends[idx] = [students1[idx], students2[idx]]
            print(friends)
        else:
            friends[idx] = [students2[idx]]
            print(friends)
            result = set()
            for s in friends[0:idx]:
                result.update(s)
            print(result)

def main():
    students1 = [1, 2, 1]
    students2 = [2, 3, 4]
    queryType = ['Friend','Friend','Total']
    n = 4
    median = getTheGroups(n, queryType, students1, students2)
    print("Total groups: ", median)


if __name__ == "__main__":
    main()