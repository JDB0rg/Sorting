# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        for smallest_index in range(i + 1, len(arr)):    
            if arr[cur_index] > arr[smallest_index]:
                cur_index = smallest_index
            
        # (hint, can do in 3 loc) 
        # TO-DO: swap
        temp = arr[i]    
        arr[i] =  arr[cur_index]
        arr[cur_index] = temp

    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print("Sorted: ",selection_sort(arr1))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr