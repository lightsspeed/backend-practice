# Function to find a maximum product of a triplet
# in array of integers of size n
def maxProduct(arr):
    n = len(arr)
    
    # Initialize Maximum, second maximum 
    # and third maximum element
    maxA = float('-inf')
    maxB = float('-inf')
    maxC = float('-inf')

    # Initialize Minimum and second minimum element
    minA = float('inf')
    minB = float('inf')

    for i in range(n):
        
        # Update Maximum, second maximum
        #and third maximum element
        if arr[i] > maxA:
            maxC = maxB
            maxB = maxA
            maxA = arr[i]
        elif arr[i] > maxB:
            maxC = maxB
            maxB = arr[i]
        elif arr[i] > maxC:
            maxC = arr[i]

        # Update Minimum and second minimum element
        if arr[i] < minA:
            minB = minA
            minA = arr[i]
        elif arr[i] < minB:
            minB = arr[i]

    return max(minA * minB * maxA, maxA * maxB * maxC)

if __name__ == "__main__":
    arr = [-10, -3, 5, 6, -20]  
    print(maxProduct(arr))
