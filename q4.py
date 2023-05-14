def count_passing_cars(A):
    n = len(A)
    east_cars = 0
    passing_cars = 0
    for i in range(n):
        if A[i] == 0:
            east_cars += 1
        else:
            passing_cars += east_cars
        if passing_cars > 1000000000:
            return -1
    return passing_cars
A = [1,0,0,0,1]
print(count_passing_cars(A))