"""
There are N students standing in a line where each student has some points. 
You distribute chocolates to these students under the following constraints: 

   1. Each student must have at least one chocolate.
   2. Students with a higher point value get more chocolates than their neighbors.

Write a method distributeChocolate to compute the minimum number of chocolates distributed such that the above conditions are satisfied.
"""
def distributeChocolate(points):
    choc = []
    for i in range(0, len(points)):
        choc.append(1)
    for i in range(0, len(points)-1):
        if points[i] > points[i+1] or points[i] > points[i-1]:
            choc[i] = choc[i] +1
        if points[i-1] > points[i+1] and points[i-1] != points[i]:
            choc[i] = choc[i] + 1
    return sum(choc)