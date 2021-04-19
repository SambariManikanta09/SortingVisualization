import time


def selectionSort(data, drawData, timeTick):
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]
                drawData(data, ['green2' if x == j or x == j +
                                1 else 'purple2' for x in range(len(data))])
                time.sleep(timeTick)


"""

data = [2, 5, 1, 7, 8]
selectionSort(data, 0, 0)
print(data)
"""
