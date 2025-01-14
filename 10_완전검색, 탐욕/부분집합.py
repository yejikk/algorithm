def printSet(n):
    global count
    count += 1
    print('{} :'.format(count), end=" ")
    for i in range(n):
        if A[i] == 1:
            print('{}'.format(data[i]), end=' ')
    print()

def powerset(n, k):
    if n == k:
        printSet(n)
    else:
        A[k] = 1
        powerset(n, k+1)
        A[k] = 0
        powerset(n, k+1)

count = 0
N = 3
A = [0 for _ in range(N)]
data = [1, 2, 3]

powerset(N, 0)