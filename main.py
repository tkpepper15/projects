#required in order to run this type of random generation.
import numpy as np

#repeats the code n times.
global n
n=int(input("Number of trials: "))

def triangle_or_not(i):

    global p
    p=0

    for i in range(n):

#randomly generates 3 unique real numbers that sum to 1 and assigns it to each side.
        arr=np.random.dirichlet(np.ones(3),size=1)
        a=(arr[0,0])
        b=(arr[0,1])
        c=(arr[0,2])

#triangle inequality theorem to determine if the sides create a triangle.
        x=0
        if c<a+b:
            x=x+1
        if a<b+c:
            x=x+1
        if b<a+c:
            x=x+1

#if all three parts of the triangle inequality theorem are met, a 1 is added to the pass (p) variable.
        if x==3:
            p=p+1

#passes (p) are divided by the total number (n) of trials to display a percentage.
if __name__ == "__main__":
    triangle_or_not(0)
result=("{:.2%}".format(p/n))
print(" ")
print(p,"were triangles and",n-p,"were not.")
print("Experimental probability:",result)
