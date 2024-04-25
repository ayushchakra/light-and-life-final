import serial
import numpy as np
from pathlib import Path

def main():
    arduino = serial.Serial(port="/dev/ttyUSB0", baudrate=119200)
    data = []
    while True:
        try:
            data.append([int(x) for x in arduino.readline().strip().decode().split(',')])
        except KeyboardInterrupt:
            break
        
    np.save(Path(__file__).parent / "data/trial_zero.npy", np.array(data))


if __name__ == "__main__":
    main()
