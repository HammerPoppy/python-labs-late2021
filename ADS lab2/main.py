def linear_search(arr, x, only_one_value):
    flag_found_number = False
    for i in range(len(arr)):
        if arr[i] == x:
            flag_found_number = True
            print('Found ' + str(x) + ' on ' + str(i) + ' index.')
            if only_one_value:
                return
    if not flag_found_number:
        print('Didnt find number' + str(x) + 'in array')


def binary_search(arr, x, only_one_value, iteration=0, flag_found_number=False):
    low = 0
    high = len(arr) - 1
    while low <= high:
        iteration += 1
        mid = (high + low) // 2
        print('low : ' + str(low))
        print('high: ' + str(high))
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            print('Found ' + str(x) + ' on ' + str(iteration) + ' iteration.')
            arr.pop(mid)
            flag_found_number = True
            if only_one_value:
                return
            else:
                binary_search(arr, x, False, iteration, True)
    if not flag_found_number:
        print('Didnt find number' + str(x) + 'in array')


def naive_search(arr, x, only_one_value=False):
    N = len(arr)
    M = len(x)

    flag_found_x = False

    for i in range(N - M + 1):
        j = 0

        while j < M:
            if arr[i + j] != x[j]:
                break
            j += 1

        if j == M:
            print("X found at index ", i)
            flag_found_x = True
            if only_one_value:
                return

    if not flag_found_x:
        print('Didnt find ' + str(x) + ' in array')


if __name__ == '__main__':
    print('creating arr:')
    arr = []
    for i in range(0, 10):
        arr.insert(2 * i, i)
        arr.insert(i, i)
        arr.insert((i + 3) * 2, i)
    print(arr)

    print('\nUsing linear search to find all 5s')
    linear_search(arr, 5, False)

    print('\nTo use binary search sorting array:')
    sorted_arr = arr.copy()
    sorted_arr.sort()
    print(sorted_arr)
    print('Searching all 3s:')
    binary_search(sorted_arr, 3, False)

    print('\nUsing unsorted array for naive search:')
    print(arr)

    print('\nSearching [4, 5, 9] sequence:')
    naive_search(arr, [4, 5, 9], False)
    print('\nSearching [5, 4] sequence:')
    naive_search(arr, [5, 4], False)
    print('\nSearching [0, 1, 2] sequence:')
    naive_search(arr, [0, 1, 2], False)
