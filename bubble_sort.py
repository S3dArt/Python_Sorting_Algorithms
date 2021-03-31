from random import randint

# Create randomized array of length 'length',
# array integers are of range
def create_array(length=10, maxint = 100):
    new_arr = [randint(0, maxint) for _ in range(length)]
    return new_arr


# apply the bubble sort algorithm to the input array
def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

    return arr


# benchmark the bubble sort against the built in python sorting method
def benchmark(n=[10, 100, 1000, 10000]):
    from time import time
    b0 = []
    b1 = []
    for length in n:
        arr = create_array(length, length)

        t0 = time()
        s_array = sorted(arr) # Sort with built in
        t1 = time()
        b1.append(t1 - t0) # record with built-in

        t0 = time()
        s_array = bubble_sort(arr) # sort with bubble sort
        t1 = time()
        b0.append(t1 - t0) # record bubble sort

    print("n \tBuilt-In\tBubble Sort")
    print("__________________________________________")
    for i, cur_n in enumerate(n):
        print(f"{cur_n} \t {b1[i]:.8f} \t {b0[i]:.5f}")


benchmark()

array = create_array()
print(array)
array = bubble_sort(array)
print(array)