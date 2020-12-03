class Example:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"My Example is X = {self.x}, Y = {self.y} and Z = {self.z}"
 
var1 = Example(1,2,3)
var2 = Example(5,2,3)

print(var1)
print(var2)