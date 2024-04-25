import serial
import numpy as np
from pathlib import Path
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import random

data = []
arduino = serial.Serial(port="/dev/ttyUSB0", baudrate=119200)


def update(frame):
    try:
        data.append([int(x) for x in arduino.readline().strip().decode().split(",")])
    except ValueError:
        return
    x = [x[0] for x in data]
    y1 = [x[1] for x in data]
    y2 = [x[2] for x in data]

    # creating a new graph or updating the graph
    graph1.set_xdata(x)
    graph1.set_ydata(y1)
    graph2.set_xdata(x)
    graph2.set_ydata(y2)
    if x[-1] - x[0] < 10000:
        plt.xlim(x[0], x[-1])
    else:
        plt.xlim(x[-1] - 10000, x[-1])


def main():
    global graph1
    global graph2

    fig, ax = plt.subplots()
    graph1 = ax.plot([0], [0], color="g")[0]
    graph2 = ax.plot([0], [0], color="r")[0]
    anim = FuncAnimation(fig, update, frames=None)
    plt.ylim(0, 260000)
    plt.legend(["IR LED Counts", "Red LED Counts"])
    plt.show()

    np.save(Path(__file__).parent / "data/trial_zero.npy", np.array(data))


if __name__ == "__main__":
    main()

# 4.5, 10, 16, 23, 30, 35, 41.9, 48.5, 54.5, 60, 66, 72, 76.5, 84.5, 89.5
