# FIND THE SPY
# The goal of this task is to write a function that is able to find the spy (if any) in a group of people.

# The function's parameters are the number of the people and a list of pairs (a list of two elements) with the following scheme:

# the first element of the pair is a number indicating a person who has information about the person in the second element of the pair.
# Example:    [[1, 2], [1, 3], [2, 3]] means that person 1 has information about person 2 and person 3, person 2 has information about person 3

# Rules:
# A spy is the person that has information about all the other people, but no one has information about the spy.
# So, in the previous example person 1 has information about all the others, but no one has information about 1 -> person 1 is the spy

# You have to return:
#  - the spy (if any): [[1, 2], [1, 3], [2, 3]] -> return 1 | [[1, 3], [2, 1], [2, 3]] -> return 2
#  - 0 if there isn't a spy ([[1, 2], [1,3], [2,3], [3,1]] -> return 0)
#  - if the number of the people is less or equals to 0, or the length of the list is grater than the number of the people or if the length of the pair is not 2 -> return -1 




x=[[1, 2], [1, 3], [2, 3]]

def findspy(x):
    length=len(x)
    for i in range(length):
        exit=0
        for j in range(length):
            if(i!=j):
                if(x[i][0]==x[j][1]):
                    exit=1
                    break
        if(not exit):
            return x[i][0]
    return 0

    
findspy(x)                    

    

