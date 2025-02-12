import math

class Vector:

    def __init__(self,*args):
        self.components=list(args)

    def __add__(self,other):
        new_components=()
        if len(self.components)!=len(other.components):
            return "Unmatching number of components"
        for i in range(len(self.components)):
            new_components=new_components+((self.components[i]+other.components[i]),)
        return Vector(new_components)

    def __sub__(self,other):
        new_components=()
        if len(self.components)!=len(other.components):
            return "Unmatching number of components"
        for i in range(len(self.components)):
            new_components=new_components+((self.components[i]-other.components[i]),)
        return Vector(new_components)
    def __mul__(self,other):
        new_components=0
        if len(self.components)!=len(other.components):
            return "Unmatching number of components"
        for i in range(len(self.components)):
            new_components=new_components+((self.components[i]*other.components[i]))
        return new_components
    def magnitude(self):
        square_product=0.0
        for i in range(len(self.components)):
            square_product+=float((self.components[i]*self.components[i]))
        return math.sqrt(square_product)

    def normalise(self):
        magnitude=self.magnitude()
        new_components=()
        for i in range(len(self.components)):
            new_components=new_components+(round(self.components[i]/magnitude,3),)
        return Vector(new_components)


    def __str__(self):
        vector="Vector( "+", ".join(map(str, self.components))+")"
        return vector

vector1=Vector(1,2,3)
vector2=Vector(3,4,5)
print(vector1)
print(vector2)
print(vector1+vector2)
print(vector1-vector2)
print(vector1*vector2)
print(vector1.magnitude())  
print(vector1.normalise())  
