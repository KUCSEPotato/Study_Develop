from random import randint

call_cnt = 0

def quicksort(array):
    global call_cnt
    call_cnt += 1
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less_than_pivot = [x for x in array[1:] if x <= pivot]
        greater_than_pivot = [x for x in array[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
    
def main():
    len_array = randint(1,100)
    random_array = [randint(1, 100) for _ in range(len_array)]
    print("Unsorted array:", random_array)
    sorted_array = quicksort(random_array)
    print("Sorted array:", sorted_array)
    print("Number of calls:", call_cnt)

if __name__ == "__main__":
    main()