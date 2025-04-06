#bubble sort
#Time : O(n^2)
#space : O(1)

A = [-5,2,5,69,7]

def bubble_sort(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                flag = True
                arr[i-1], arr[i] = arr[i], arr[i-1]


bubble_sort(A)
print(A)

