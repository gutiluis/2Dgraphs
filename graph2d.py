#!/usr/bin/env python3

# file: graph2d.py
# descr: script to make a 2D cardinal graph

from matplotlib import pyplot


def graph_vectors():
    x_values = []
    y_values = []

    for i in range(12):
        x, y = input(f"Enter vector {i + 1} (x,y): ").strip().split(",")

        x_values.append(int(x))
        y_values.append(float(y))

    pyplot.plot(x_values, y_values, marker="o", label="Vectors")

    pyplot.axhline(y=0, color="black")
    pyplot.axvline(x=0, color="black")

    pyplot.xlabel("X")
    pyplot.ylabel("Y")

    pyplot.grid(True)
    pyplot.legend()

    pyplot.show()


if __name__ == "__main__":
    graph_vectors()
