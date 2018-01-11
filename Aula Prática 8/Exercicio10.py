def quicksort(arr):
    high = []
    low = []
    pivot_list = []

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                low.append(i)
            elif i > pivot:
                high.append(i)
            else:
                pivot_list.append(i)
        high = quicksort(high)
        low = quicksort(low)

    return low + pivot_list + high

print(quicksort([6,2,5,3,1,8,4,7,5,9]))