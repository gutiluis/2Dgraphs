#!/usr/bin/env python3

# file: 2dgrapher.py
# descr: script to make a 2d graph



from matplotlib import pyplot

x_start, x_end = map(int, input("Enter the range of x (e.g. -6,3): ").split(","))




y_start, y_end = map(int, input("Enter the range of y (e.g. -6,3: ").split(","))


list_x = list(range(x_start, x_end + 1))
list_y = list(range(y_start, y_end + 1))




# graph blue line
pyplot.plot(list_x, list_y, label="y", color="blue", linewidth=2)

pyplot.axhline(y=0, color="black")
pyplot.axvline(x=0, color="black")



pyplot.xlabel("X input")
pyplot.ylabel("Y input")

pyplot.grid(True)

pyplot.show()
