from time import time
from fun_quickSort import quick_sort
from tkinter import *
from tkinter import ttk
import random
from fun_mergeSort import merge_sort
from fun_bubbleSort import bubble_sort
from fun_selectSort import selectionSort
from fun_insertSort import insertionSort

root = Tk()

root.title("Sorting Alorithm Visualization")
root.maxsize(900, 600)
root.config(bg='black')

# variables
selected_alg = StringVar()
data = []

# function definations


def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 10
    spacing = 10
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        # top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340

        # bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fil=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

    root.update_idletasks()


def Generate():
    global data
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    if minVal > maxVal:
        minVal, maxVal = maxVal, minVal

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    # data = [100, 20, 40, 60, 50, 30, 10, 85]
    # not sorted array
    drawData(data, ["purple2" for x in range(len(data))])


def startSorting():
    global data
    timeTaken = speedScale.get()
    if not data:
        return
    elif algMenu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, timeTaken)
    elif algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, timeTaken)
    elif algMenu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data)-1, drawData, timeTaken)

    elif algMenu.get() == "Selection Sort":
        selectionSort(data, drawData, timeTaken)

    elif algMenu.get() == "Insertion Sort":
        insertionSort(data, drawData, timeTaken)

    drawData(data, ['green2' for x in range(len(data))])

 # frame / base layout


UI_frame = Frame(root, width=600, height=200, bg='orange')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='snow')
canvas.grid(row=1, column=0, padx=10, pady=5)

# User Interface Area
# Row[0]
Label(UI_frame, text="Algorithm: ", bg='snow').grid(
    row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg,
                       values=['Selection Sort', 'Bubble Sort',  'Insertion Sort', 'Merge Sort', 'Quick Sort',  'Radix Sort',  'Heap Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2,
                   resolution=0.2, orient=HORIZONTAL, label="Select Speed[s]")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="! Start !", command=startSorting).grid(
    row=0, column=3, padx=5, pady=5)


"""
Generate button with Red color 
Button(UI_frame, text="Generate", command=Generate,
       bg='red').grid(row=0, column=2, padx=5, pady=5)
"""


# Row[1]
# Label(UI_frame, text="Size: ", bg='grey').grid(  row=1, column=0, padx=5, pady=5, sticky=W)
# For input from the user| sizeEntry = Entry(UI_frame)

sizeEntry = Scale(UI_frame, from_=3, to=25,
                  resolution=1, orient=HORIZONTAL, label="Data Size:")
sizeEntry.grid(row=1, column=0, padx=5, pady=5, sticky=W)

# Label(UI_frame, text="Min_Value: ", bg='grey').grid(    row=1, column=2, padx=5, pady=5, sticky=W)
# For input from the user| minEntry = Entry(UI_frame)
minEntry = Scale(UI_frame, from_=0, to=100,
                 resolution=1, orient=HORIZONTAL, label="Minimum")
minEntry.grid(row=1, column=1, padx=5, pady=5, )

# Label(UI_frame, text="Max_Value: ", bg='grey').grid(   row=1, column=4, padx=5, pady=5, sticky=W)
# For input from the user |maxEntry = Entry(UI_frame)
maxEntry = Scale(UI_frame, from_=10, to=1000,
                 resolution=1, orient=HORIZONTAL, label="Maximum ")
maxEntry.grid(row=1, column=2, padx=5, pady=5, )


# Generate Button

Button(UI_frame, text="Generate", command=Generate, bg="snow").grid(
    row=1, column=5, padx=5, pady=5)


root.mainloop()
