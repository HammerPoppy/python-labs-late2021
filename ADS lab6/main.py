from heapq import *

if __name__ == '__main__':
    print('creating heap')
    heap = []
    print(heap)

    print('\nadding item to heap')
    heappush(heap, 3)
    print(heap)

    print('\nand another one')
    heappush(heap, 1)
    print(heap)

    print('\ngetting the smallest item without deleting it')
    print(heap[0])
    print(heap)

    print('\ngetting the smallest item and deleting it')
    print(heappop(heap))
    print(heap)

    heappush(heap, 6)
    print(heap)
    print('\nadding item and also deleting the smallest one')
    heappushpop(heap, 5)
    print(heap)

    print('\nadding item and also deleting the smallest one, but it is more efficient that pop than push and'
          'also returning value')
    heapreplace(heap, 9)
    print(heap)
