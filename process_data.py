from pathlib import Path
import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt

ARDUINO_DATA_FP = Path(__file__).parent / "data/trial_zero.npy"
EMG_DATA_FP = Path(__file__).parent / "data/processed_data.mat"
EMG_SAMPLING_RATE = 100  # Hz

timestamp_setpoints = [4500, 10000]


def main():
    light_data = np.load(ARDUINO_DATA_FP)
    emg_data = loadmat(EMG_DATA_FP)["processed"]
    curr_timestamp_setpoint_idx = 0
    for idx, (timestamp, redReading, irReading) in enumerate(light_data):
        if timestamp > timestamp_setpoints[curr_timestamp_setpoint_idx]:
            fig, ax1 = plt.subplots()
            ax1.set_xlabel("Time [s]")
            lns1 = ax1.plot(
                np.linspace(0, 1.4, 1400),
                emg_data[curr_timestamp_setpoint_idx, :, 0],
                "g",
                label="EMG Data",
            )
            ax2 = ax1.twinx()
            lns2 = ax2.plot(
                (light_data[idx - 1 : idx + 5, 0] - light_data[idx - 1, [0]]) / 1000,
                light_data[idx - 1 : idx + 5, 1],
                "r",
                label="Red LED Data",
            )
            lns = lns1 + lns2
            labs = [l.get_label() for l in lns]
            ax1.legend(lns, labs)
            ax1.spines["left"].set_color("green")
            ax2.spines["left"].set_color("green")
            ax1.spines["right"].set_color("red")
            ax2.spines["right"].set_color("red")
            ax1.tick_params(axis="y", colors="green")
            ax2.tick_params(axis="y", colors="red")
            ax1.yaxis.label.set_color("green")
            ax2.yaxis.label.set_color("red")
            ax1.set_ylabel("ADC Reading [counts]")
            ax2.set_ylabel("ADC Reading [counts]")
            plt.savefig(Path(__file__).parent / f"imgs/trial_{curr_timestamp_setpoint_idx}_red.png")

            fig, ax1 = plt.subplots()
            ax1.set_xlabel("Time [s]")
            lns1 = ax1.plot(
                np.linspace(0, 1.4, 1400),
                emg_data[curr_timestamp_setpoint_idx, :, 0],
                "g",
                label="EMG Data",
            )
            ax2 = ax1.twinx()
            lns2 = ax2.plot(
                (light_data[idx - 1 : idx + 5, 0] - light_data[idx - 1, [0]]) / 1000,
                light_data[idx - 1 : idx + 5, 2],
                "r",
                label="IR LED Data",
            )
            lns = lns1 + lns2
            labs = [l.get_label() for l in lns]
            ax1.legend(lns, labs)
            ax1.spines["left"].set_color("green")
            ax2.spines["left"].set_color("green")
            ax1.spines["right"].set_color("red")
            ax2.spines["right"].set_color("red")
            ax1.tick_params(axis="y", colors="green")
            ax2.tick_params(axis="y", colors="red")
            ax1.yaxis.label.set_color("green")
            ax2.yaxis.label.set_color("red")
            ax1.set_ylabel("ADC Reading [counts]")
            ax2.set_ylabel("ADC Reading [counts]")
            plt.savefig(Path(__file__).parent / f"imgs/trial_{curr_timestamp_setpoint_idx}_ir.png")
            breakpoint()
            curr_timestamp_setpoint_idx += 1
            if curr_timestamp_setpoint_idx == len(timestamp_setpoints):
                break


if __name__ == "__main__":
    main()
