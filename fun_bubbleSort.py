import time


def bubble_sort(data, drawData, timeTick):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['green2' if x == j or x == j +
                                1 else 'purple2' for x in range(len(data))])
                time.sleep(timeTick)
    #drawData(data, ['green2' for x in range(len(data))])

# return data


"""
data = [2, 4, 1, 7, 2, 8]
data = bubble_sort(data)
print(data)
"""
