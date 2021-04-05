from random import randint


# контсруктор массива
def create_array(size=10, max=100):
    return [randint(0, max) for _ in range(size)]


# ставим перегородки
def partition(a, low, high):
    i = low - 1
    pivot = a[high]
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


def quicksort_inplace(arr, low=0, high=None):
    if high == None:
        high = len(arr) - 1
    if low < high:
        p_idx = partition(arr, low, high)  # перегородка вокруг оси
        quicksort_inplace(arr, low, p_idx - 1)  # сортировать нижнюю половину
        quicksort_inplace(arr, p_idx + 1, high)  # сортировать верхнуюю половину


def benchmark(n=[10, 100, 1000, 10000]):
    from time import time
    b0 = []
    b1 = []
    for length in n:
        arr = create_array(length, length)
        t0 = time()
        s_array = sorted(arr)
        t1 = time()
        b1.append(t1 - t0)

        t0 = time()
        quicksort_inplace(arr)
        t1 = time()
        b0.append(t1 - t0)

    print("n \tBuilt-In\tInserti Sort")
    print("_______________________________________")
    for i, cur_n in enumerate(n):
        print(f"{cur_n} \t {b1[i]:.8f} \t {b0[i]:.6f}")


a = create_array()
print(a)
quicksort_inplace(a)
print(a)

benchmark()