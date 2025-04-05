def thirdLargest(arr):

    n = len(arr)

    first, second, third = float('-inf'), float('-inf'), float('-inf')

    for i in range(n):
        
        if arr[i] > first:

            third = second
            second = arr[i]

        elif arr[i] > second:
            third = second
            second = arr[i]

        elif arr[i] > third:
            third = arr[i]
    
    return third

if __name__ == "__main__":

    arr = [1, 4, 11, 52, 148, 100]

    print(thirdLargest(arr))


# first = -∞
# second = -∞
# third = -∞

# i = 0, arr[0] = 1:
# Copyif arr[i](1) > first(-∞):
#     third = second(-∞)
#     second = first(-∞)
#     first = arr[i](1)
# After this: first = 1, second = -∞, third = -∞
# 
# 
# 
# i = 1, arr[1] = 4:
# Copyif arr[i](4) > first(1):
#     third = second(-∞)
#     second = first(1)
#     first = arr[i](4)
# After this: first = 4, second = 1, third = -∞
#
# 
# 
#  i = 2, arr[2] = 11:
# Copyif arr[i](11) > first(4):
#     third = second(1)
#     second = first(4)
#     first = arr[i](11)
# After this: first = 11, second = 4, third = 1
#
# 
#  i = 3, arr[3] = 52:
# Copyif arr[i](52) > first(11):
#     third = second(4)
#     second = first(11)
#     first = arr[i](52)
# After this: first = 52, second = 11, third = 4
# 
# 
# i = 4, arr[4] = 148:
# Copyif arr[i](148) > first(52):
#     third = second(11)
#     second = first(52)
#     first = arr[i](148)
# After this: first = 148, second = 52, third = 11
# 
# 
# i = 5, arr[5] = 100:
# Copyif arr[i](100) > first(148):
#     // This is false
# elif arr[i](100) > second(52) and arr[i](100) < first(148):
#     third = second(52)
#     second = arr[i](100)
# After this: first = 148, second = 100, third = 52
# Result: The function returns third = 52
# The original code had a logical error in the second condition where it wasn't checking if the current element is less than the first largest, which could cause incorrect results when there are duplicate values.