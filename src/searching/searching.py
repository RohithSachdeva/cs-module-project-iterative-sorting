def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    
        return -1   # not found


# Write an iterative implementation of Binary Search
#Expects a sorted array of integers

def binary_search(arr, target):
    #Assumption is a sorted array; lowest is the 0th index .. highest the last
    low = 0
    high = len(arr) - 1
    # Your code here

    #Binary search looks for the middle of the array 
    while low <= high: 
        middle = (low + high) // 2
        guess = arr[middle]
        if guess == target: #You guessed correctly; return the middle
            return middle
        if guess > target: #You want to shorten the array behind the midpoint by decreasing the range
            high = middle - 1 
        else: #If the guess is less... you need to choose a later starting point;  increase low ... 
            low = middle + 1

    return -1  # not found
