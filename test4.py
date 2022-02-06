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

class Intersec:

    def __init__(self,cube1,cube2,x1,y1,z1,x2,y2,z2):
        self.cube1=cube1
        self.cube2=cube2
        self.x1=x1
        self.y1=y1
        self.z1=z1
        self.x2=x2
        self.y2=y2
        self.z2=z2


    def inter(self):
        X1min=self.x1-(self.cube1/2) #for cube1 x-minimum
        Y1min=self.y1-(self.cube1/2) #for cube1 y-minimum
        Z1min=self.z1-(self.cube1/2) #for cube1 z-minimum
        X2max=self.x2+(self.cube2/2) #for cube2 x-maximum
        Y2min=self.y2-(self.cube2/2) #for cube2 y-minimum
        Y2max=self.y2+(self.cube2/2) #for cube2 y-maximum
        Z2max=self.z2+(self.cube2/2) #for cube2 z-maximum
        if X1min>X2max and Y1min>Y2max and Z1min>Z2max:
            return False
        a=[]
        if X2max>X1min:
            a.append(X2max-X1min)

        if Y2max>Y2min:
            a.append(Y2max-Y2min)    
        if self.z1==0 or self.z2==0:
            a.append(float(self.cube2))
        elif Z2max>Z1min:
            a.append(Z2max-Z1min) 
        intersection=1
        for i in a:
            intersection*=i     
        return True, intersection 

inters=Intersec(5,2,10,10,0,8,9,0)   
inters.inter()           
 
