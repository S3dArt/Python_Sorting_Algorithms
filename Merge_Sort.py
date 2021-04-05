# конструктор массива
def create_array(size=10, max=100):
    from random import randint
    return [randint(0, max) for _ in range(size)]


def merge(a, b):
    c = []  # финальный выходной массив
    a_idx, b_idx = 0, 0
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            c.append(a[a_idx])
            a_idx += 1
        else:
            c.append(b[b_idx])
            b_idx += 1

    if a_idx == len(a):
        c.extend(b[b_idx:])
    else:
        c.extend(a[a_idx:])
    return c


def merge_sort(arr):
    # список из нуля или одного элемента сортируется по определению
    if len(arr) <= 1:
        return arr

    # разделить список пополам и рекурсивно вызвать сортировку слиянием для каждого
    left, right = merge_sort(arr[:len(arr)//2]), merge_sort(arr[len(arr)//2:])

    # слияние подсписка
    return merge(left, right)

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
        s_array = merge_sort(arr)
        t1 = time()
        b0.append(t1 - t0)

    print("n \tBuilt-In\tInserti Sort")
    print("_______________________________________")
    for i, cur_n in enumerate(n):
        print(f"{cur_n} \t {b1[i]:.8f} \t {b0[i]:.6f}")


a = create_array()
print(a)
s = merge_sort(a)
print(s)

benchmark()

