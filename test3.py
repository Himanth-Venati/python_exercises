# Find the non-duplicate number

# Given an array like this [4,3,2,1,4,3,2] find the number that appears only once in the array, in this case is 1.

# Other examples:
# [1,1,2,2,3,3,4,4,5] --> 5
# [1,2,3,4,1,3,4] --> 2

list=[4,3,2,1,4,3,2]
count={}
for i in list:
    count[i]=count.get(i,0)+1
for key,value in count.items():
    if value==1:
        print(key) 