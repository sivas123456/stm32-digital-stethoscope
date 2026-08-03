# STM32 Digital Stethoscope

An embedded biomedical signal acquisition system built on the STM32F407VG microcontroller, featuring real-time heart sound amplification, ADC digitization, UART-based data streaming, digital signal smoothing, and Python-based waveform visualization.

## 📖 Project Overview
The STM32 Digital Stethoscope is a complete end-to-end biomedical data acquisition project. It captures analog heart sound signals using a MAX9814 microphone amplifier, digitizes the signal via the STM32F407VG's built-in ADC, and streams the data over USART to a PC. On the PC, Python scripts parse, filter, and visualize the heart sound waveforms in real-time, simulating a digital stethoscope display.

## 🌟 Features
- **Real-Time Signal Acquisition**: Continuous 12-bit ADC sampling of heart sounds at ~1 kHz.
- **Hardware Amplification**: High-gain analog signal conditioning using the MAX9814 module.
- **Serial Data Streaming**: Robust UART transmission of digitized samples to a host PC.
- **Real-Time Visualization**: Python-based scrolling plots for instant waveform feedback.
- **Digital Signal Processing**: Moving average filtering for noise reduction and signal smoothing.

## 🏗️ System Architecture
### Hardware Components
- **Microcontroller**: STM32F407VG Discovery Board / Custom PCB
- **Sensor/Amplifier**: MAX9814 Microphone Amplifier
- **Communication Interface**: USB-to-UART Bridge (CP2102/CH340) or on-board ST-LINK Virtual COM Port
- **Cables/Connectors**: Jumper wires, USB cables for programming and serial monitoring

### Software Stack
- **Firmware**: Embedded C (STM32 HAL Library)
- **IDE**: STM32CubeIDE
- **Host PC Scripts**: Python 3.x
- **Visualization Libraries**: Matplotlib, NumPy, IPython

## 📂 Folder Structure
```text
stm32-digital-stethoscope/
│
├── Firmware/
│   ├── Core/
│   │   ├── Inc/           # Header files
│   │   └── Src/           # Source files (main.c)
│   ├── Drivers/           # HAL driver files
│   └── Startup/           # Startup code
│
├── Python/
│   ├── realtime_plot.py   # Simulates real-time waveform plotting
│   └── waveform_plot.py   # Smooths and plots zoomed-in waveforms
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## 🔌 Circuit Overview
1. **MAX9814 VDD** -> STM32 3.3V
2. **MAX9814 GND** -> STM32 GND
3. **MAX9814 OUT** -> STM32 PA0 (ADC1_IN0)
4. **STM32 USART2 TX (PA2)** -> PC RX (via USB-TTL)
5. **STM32 USART2 RX (PA3)** -> PC TX (via USB-TTL)

## ⚙️ Working Principle
### 1. Signal Acquisition Pipeline
```text
MAX9814 Microphone
       ↓
Analog Amplification
       ↓
STM32F407VG ADC Sampling
       ↓
USART Data Transmission
       ↓
Python Data Acquisition
       ↓
Moving Average Filtering
       ↓
Real-Time Waveform Visualization
```

### 2. Firmware Architecture
- The system initializes the system clock, GPIO, ADC1, and USART2.
- The main `while(1)` loop starts an ADC conversion and waits for completion (`HAL_ADC_PollForConversion`).
- The 12-bit ADC value (0-4095) is read, formatted into a string using `sprintf`, and transmitted over USART2.
- A 1 ms delay enforces a sampling rate of ~1 kHz, adequate for capturing standard heart sound frequencies (20 Hz - 200 Hz).

### 3. Signal Processing Pipeline (Python)
- Data received from the UART stream is saved to a text file.
- Python scripts read the logged data and parse it into an array of integers.
- `waveform_plot.py` applies a moving average filter using `numpy.convolve` to smooth the signal and remove high-frequency noise.
- `matplotlib` and `IPython.display` are used to animate the waveform, simulating the scrolling display of a medical monitor.

## 🚀 Installation & Usage

### 1. Firmware Flashing
1. Open the `Firmware/` project in STM32CubeIDE.
2. Build the project (`Project > Build All`).
3. Connect your STM32 board via USB.
4. Flash the code to the microcontroller (`Run > Debug` or `Run > Run`).

### 2. Python Environment Setup
Ensure you have Python 3 installed. Navigate to the project root and install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Running the Visualization
1. Connect the UART interface and use a serial terminal (e.g., TeraTerm, PuTTY) to log the incoming data to a file named `seee.txt` inside the `Python/` directory.
2. Run the visualization scripts:
```bash
cd Python
python realtime_plot.py
# or
python waveform_plot.py
```

## 🛠️ Technologies Used
- **Embedded Systems**: STM32, ARM Cortex-M4, ADC, UART
- **Languages**: C, Python
- **Data Processing**: NumPy, DSP (Moving Average Filter)
- **Data Visualization**: Matplotlib

## 🔮 Future Improvements
- **Direct Serial Reading in Python**: Replace the file-based (`seee.txt`) approach with direct real-time serial port reading using `pyserial`.
- **Advanced Digital Filtering**: Implement FIR/IIR bandpass filters directly on the STM32 using ARM CMSIS-DSP library.
- **Bluetooth Streaming**: Replace UART with an HC-05 or ESP32 module for wireless stethoscope capabilities.
- **OLED Display**: Add an I2C OLED screen for local waveform rendering directly on the device.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
