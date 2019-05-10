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

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    should_continue = True
    while should_continue:
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                i += 1
            elif arr[i] < arr[i + 1]:
                i += 1
                should_continue = True
            elif arr[i] < arr[i + 1] in range(0, len(arr) - 1):
                should_continue = False
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr