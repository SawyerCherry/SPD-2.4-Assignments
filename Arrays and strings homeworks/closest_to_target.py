def distance_to_t(t, x):
    return abs(t - x)

def closestToT(arrayA, arrayB, T):
    val_a = 0
    val_b = 0
    smallestNum = 10000
    for i in range(len(arrayA)):
        for j in range(len(arrayB)): 
            numApart = distance_to_t(T, (arrayA[i] + arrayB[j]))
            if smallestNum > numApart or smallestNum == numApart:
                smallestNum = numApart
                val_a = arrayA[i]
                val_b = arrayB[j]
    print([val_a, val_b])

a=[9, 13, 1, 8, 12, 4, 0, 5]
b=[3, 17, 4, 14, 6]
t=20
closestToT(a,b,t)