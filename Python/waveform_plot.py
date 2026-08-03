import matplotlib.pyplot as plt
import time
from IPython.display import clear_output
import numpy as np

# Parameters
fs = 1000  # sampling rate in Hz (adjust as per your data)
window_size = 50  # moving average window to smooth
buffer_size = 250  # fewer points to zoom in
step_size = 5
delay = 0.1  # slow playback to visualize beats

# Load data
with open("seee.txt", "r") as f:
    raw_data = f.read()

# Parse ADC values
values = [int(val) for val in raw_data.strip().split("\n") if val.isdigit()]
values = np.array(values)

# Apply simple smoothing (optional)
smoothed = np.convolve(values, np.ones(window_size)/window_size, mode='valid')

# Real-time simulation
for i in range(0, len(smoothed) - buffer_size, step_size):
    chunk = smoothed[i:i+buffer_size]
    time_axis = np.arange(len(chunk)) / fs  # time in seconds

    clear_output(wait=True)
    plt.figure(figsize=(10, 4))
    plt.plot(time_axis, chunk)
    plt.ylim(0, 4095)
    plt.title("Heart Sound Waveform (Zoomed in)")
    plt.xlabel("Time (s)")
    plt.ylabel("ADC Value")
    plt.grid(True)
    plt.show()

    time.sleep(delay)
