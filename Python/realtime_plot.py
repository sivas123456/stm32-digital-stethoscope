import matplotlib.pyplot as plt
import time
from IPython.display import clear_output

# Load the data
with open("seee.txt", "r") as f:
    raw_data = f.read()

# Parse integer values
values = [int(val) for val in raw_data.strip().split("\n") if val.isdigit()]

# Playback settings
buffer_size = 500
step_size = 10
delay = 0.05

# Scroll through the data
for i in range(0, len(values) - buffer_size, step_size):
    chunk = values[i:i+buffer_size]
    
    clear_output(wait=True)  # Clear previous plot
    
    plt.figure(figsize=(10, 4))
    plt.plot(chunk)
    plt.ylim(0, 4095)
    plt.title("Simulated Real-Time Heart Sound Waveform")
    plt.xlabel("Sample Index")
    plt.ylabel("ADC Value")
    plt.grid(True)
    plt.show()
    
    time.sleep(delay)
