# Create a small  application that  accepts the dimensions and coordinates of two cubic objects in a 3-dimensional space. 
# The two cubes are parallel to each other (they are not rotated in any way).  The  application should calculate if the two cubes intersect, and if so, what the volume of the shared space is.
# Sample Data
# Cube A:
# Size = 5m

# x = 10m
# y = 10m
# z = 0

# Cube B:
# Size = 2m

# x = 9m
# y = 9m
# z = 0
# It should return:
# A boolean indicating it the cubes intersect
# and the volume of the shared space, if the cubes do not intersect then this should be 0
# I did not understand this , can you please help me with the explanation

def inter(cube1,cube2,Dcube1,Dcube2):
    T1=[]  
    for i in Dcube1:
        T1.append(i+cube1)
    T2=[]   
    for i in Dcube2:
        T2.append(i+cube2) 
    inter1=[]    
    for n in range(0,len(T2)):
        if T2[n]>Dcube1[n]:
            inter1.append(T2[n]-Dcube1[n])
            True
        else:
            print('0 intersection')    
    return inter1    
     
                   
inter(5,2,[10,10,0],[9,9,0])    
