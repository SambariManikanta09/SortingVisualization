import time


def insertionSort(data, drawData, timeTick):
    for i in range(len(data)):
        j = i
        while j > 0 and data[j-1] > data[j]:
            data[j-1], data[j] = data[j], data[j-1]
            j -= 1
        drawData(data, ['green2' if x == j or x == j +
                        1 else 'purple2' for x in range(len(data))])
        time.sleep(timeTick)


"""
data = [1, 4, 2, 5, 3]
insertionSort(data, 0, 0)
print(data)
"""
