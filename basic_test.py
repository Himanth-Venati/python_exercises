#@function called print_results which takes no arguments and returns:
# 1. Strive if the number is divisible by 3
# 2. School if the number is divisible by 5
# 3. Strive School if the number is divisible by 3 and 5
# 4. The same number otherwise (if the number is not divisible neither by 3 and neither by 5)
import numpy as np
x=np.array([5,3,15])
def print_results(x):
    for num in x:

        if num % 3 == 0 and num % 5 ==0:
            print('strive school')
        elif num % 3 == 0:
            print('strive')
        elif num % 5 == 0:
            print('school')
    
        else:
            print(num)
    return
print_results(x)    

