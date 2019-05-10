# 1. While your data set contains more than one item, split it in half
# 2. Once you have gotten down to a single element, you have also *sorted* that element 
#    (a single element cannot be "out of order")
# 3. Start merging your single lists of one element together into larger, sorted sets
# 4. Repeat step 3 until the entire data set has been reassembled

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    i = 0
    j = 0
    for i in range(elements):
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        elif arrA[i] >= arrB[j]:
            merged_arr.append(arrB[j])
            j += 1
        elif i >= len(arrA):
            merged_arr.append(arrB[j])
            j += 1
        else:
            merged_arr.append(arrA[i])
            i  += 1
    print("M", merged_arr)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        low = merge_sort(arr[0: len(arr) / 2])
        high = merge_sort(arr[len(arr) / 2: ])
        
        arr = merge(low, high)
    return arr

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
