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

# x = 8m
# y = 9m
# z = 0
# It should return:
# A boolean indicating it the cubes intersect
# and the volume of the shared space, if the cubes do not intersect then this should be 0

cube1=5
cube2=2
Dcube1=[10,10,0]
Dcube2=[8,9,0]
def inter(cube1,cube2,x1,y1,z1,x2,y2,z2):
    X1min=x1-(cube1/2) # for cube1 x-minimum
    Y1min=y1-(cube1/2) #for cube1 y-minimum
    Z1min=z1-(cube1/2) #for cube1 z-minimum
    X2max=x2+(cube2/2) # for cube2 x-maximum
    Y2min=y2-(cube2/2) #for cube2 y-minimum
    Y2max=y2+(cube2/2) # for cube2 y-maximum
    Z2max=z2+(cube2/2) # for cube2 z-maximum
    if X1min>X2max:
        return 0
    if Y1min>Y2max:
        return 0
    if Z1min>Z2max:
        return 0   
    a=[]
    if X2max>X1min:
        a.append(X2max-X1min)

    if Y2max>Y2min:
        a.append(Y2max-Y2min)    
    if z1==0 or z2==0:
        a.append(float(cube2))
    elif Z2max>Z1min:
        a.append(Z2max-Z1min)
    if a!=0:
        intersection=['True',a[0]*a[1]*a[2]] 

    else:
        return False   
    return intersection          
inter(5,2,10,10,0,8,9,0)  
