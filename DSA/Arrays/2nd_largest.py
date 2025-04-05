def getSecondLargest(arr):
    # Handle edge cases
    if len(arr) < 2:
        return None  # Cannot find second largest with fewer than 2 elements
    
    # Initialize both largest and second largest
    largest = float('-inf')
    secondLargest = float('-inf')
    
    # Iterate starting from the third element
    for i in range(2, len(arr)):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
        elif arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]
    
    return secondLargest

# Example usage
if __name__ == "__main__":
    arr = [12, 8, 41, 27, 1, 59]
    result = getSecondLargest(arr)
    print(f"The second largest element is: {result}")



#Dry run above code:

# for i in range(2, len(arr)):
#         if arr[i](41) > largest(-1):
#             secondLargest = largest
#             largest = arr[i](41)
#         elif arr[i] > secondLargest and arr[i] != largest:
#             secondLargest = arr[i]
    

# for i in range(2, len(arr)):
#         if arr[i](27) > largest(41):
#             secondLargest = largest
#             largest = arr[i]
#         elif arr[i](27) > secondLargest(-1) and arr[i](27) != largest(41):
#             secondLargest = arr[i](27)
    
# for i in range(2, len(arr)):
#         if arr[i](1) > largest(41):
#             secondLargest = largest
#             largest = arr[i]
#         elif arr[i](1) > secondLargest(27) and arr[i](1) != largest(41):
#             secondLargest = arr[i](27)



#for i in range(2, len(arr)):
#         if arr[i](59) > largest(41):
#             secondLargest (41)= largest
#             largest = arr[i](59)
#         elif arr[i](1) > secondLargest(27) and arr[i](1) != largest(41):
#             secondLargest = arr[i](27)