def create_array(length=10, max_int=100):
    from random import randint
    return [randint(0, max_int) for _ in range(length)]

# алгоритм сортировки вставками на переданном списке
# возвращает отсортированную версию списка

def insertion_sort_bad(arr):
    for i in range(1, len(arr)):
        j = i - 1
        nxt_element = arr[i]

        # Сравниваем текущий элемент со следующим
        while (j >= 0) and (arr[j] > nxt_element):
            arr[j] = nxt_element
            j -= 1


# более наглядная реализация
def insertion_sort(arr):
    for sort_len in range(1, len(arr)):
        cur_item = arr[sort_len]  # следующая неотсортированная позиция
        insert_idx = sort_len  # текущий индекс позиции

        # итерация, пока не достигнем правильного места вставки
        while insert_idx > 0 and cur_item < arr[insert_idx - 1]:
            arr[insert_idx] = arr[insert_idx - 1]  #сдвигаем
            insert_idx -= 1

        # вставляем элемент в текущее место которого достигли index_idx
        arr[insert_idx] = cur_item

    return arr


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
        s_array = insertion_sort(arr)
        t1 = time()
        b0.append(t1 - t0)

    print("n \tBuilt-In\tInserti Sort")
    print("_______________________________________")
    for i, cur_n in enumerate(n):
        print(f"{cur_n} \t {b1[i]:.8f} \t {b0[i]:.6f}")


a = create_array()
print(a)
a = insertion_sort(a)
print(a)

benchmark()
