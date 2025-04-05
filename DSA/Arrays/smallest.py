def findSmallestAndSecondSmallest(arr):
    if len(arr) < 2:
        return "Array should have at least 2 elements"
    
    smallest = second_smallest = float('inf')
    
    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    
    if second_smallest == float('inf'):
        return smallest, "No second smallest element"
    else:
        return smallest, second_smallest
    

if __name__ == "__main__":

    arr = [12, 5, 7, 5, 11, 3, 8, 2]



    print(findSmallestAndSecondSmallest(arr))