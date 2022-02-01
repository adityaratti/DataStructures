def insertion_sort(arr):
    for i in range(1, len(arr)):
        curr = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > curr:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = curr

    print(arr)


insertion_sort([1, 2, 3, 18, 4, 6, 10, 8])
insertion_sort(['A', 'C', 'B', 'F', 'X', 'I'])


def merge_sort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)

        merge(arr, l, m, r)


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    arr1 = [None] * n1
    arr2 = [None] * n2
    for i in range(n1):
        arr1[i] = arr[l + i]
    for j in range(n2):
        arr2[j] = arr[m + 1 + j]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = arr1[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = arr2[j]
        j += 1
        k += 1

merge_arr = [1, 2, 3, 18, 4, 6, 10, 8]
merge_sort(merge_arr, 0, 7)
print(merge_arr)

def quick_sort(arr, low, high):
    if low < high:
        i_part = partition(arr, low, high)
        quick_sort(arr, low, i_part -1)
        quick_sort(arr, i_part + 1, high)


def partition(arr, low, high):
    pivot = arr[high]

    i_small = low - 1

    for i in range(low,     high-low):
        if arr[i] < pivot:
            i_small += 1
            arr[i], arr[i_small] = arr[i_small], arr[i]


    arr[high], arr[i_small+1] = arr[i_small+1], arr[high]

    return i_small+1

quick_arr = [10,20,80,90,60,15,70]
quick_sort(quick_arr, 0, len(quick_arr) -1)
print(quick_arr)


def binary_search(arr, low, high, key):
    if low >= high:
        return -1
    mid = low + (high - low) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, low, mid - 1, key)
    else:
        return binary_search(arr, mid + 1, high, key)

arr = [2, 3, 4, 5, 8, 10]
x = 8
result = binary_search(arr, 0, len(arr) - 1, x)
print(result)

def heapify(arr, n, i):
    largest = i
    l = 2 * i +1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = [12,11,13,5,6,7]
heapsort(arr)
print("Sorted array is ", arr)

