def create_array(length=10, maxint=100):
    from random import randint
    return [randint(0, maxint) for _ in range(length)]


# performs the selection sort algorithm on the passed
# list, returns the sorted version
def selection_sort(arr):
    sort_len = 0  # length of current sorted portion
    while sort_len < len(arr):
        min_idx = None  # index of smallest item found
        for i, elem in enumerate(arr[sort_len:]):
            # check current elem to see if smallest
            if min_idx == None or elem < arr[min_idx]:
                # update with current smaller
                min_idx = i + sort_len
        arr[sort_len], arr[min_idx] = arr[min_idx], arr[sort_len]
        sort_len += 1
    return arr


# other version selection sort
def selection_sort_other(arr):
    for idx in range(len(arr)):
        min_idx = idx
        for j in range(idx + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        # Swap the minimum value with the compared value
        arr[idx], arr[min_idx] = arr[min_idx], arr[idx]


# benchmark the bubble sort against the built in python sorting method
def benchmark(n=[10, 100, 1000, 10000]):
    from time import time
    b0 = []
    b1 = []
    for length in n:
        arr = create_array(length, length)

        t0 = time()
        s_array = sorted(arr)  # Sort with built in
        t1 = time()
        b1.append(t1 - t0)  # record with built-in

        t0 = time()
        s_array = selection_sort(arr) # sort with bubble sort
        t1 = time()
        b0.append(t1 - t0)  # record bubble sort

    print("n \tBuilt-In\tBubble Sort")
    print("__________________________________________")
    for i, cur_n in enumerate(n):
        print(f"{cur_n} \t {b1[i]:.8f} \t {b0[i]:.5f}")


a = create_array()
print("Unsorted:", a)
a = selection_sort(a)
print("Sorted:", a)


benchmark()