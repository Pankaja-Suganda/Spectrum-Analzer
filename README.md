# Spectrum Analyzer GUI

This project aims to create a Spectrum Analyzer Graphical User Interface (GUI) using Python's Tkinter library and Matplotlib. The GUI visualizes frequency and power data obtained from a connected device through a serial port. It provides real-time updates of the spectrum data, allowing users to analyze frequency distribution and power levels.

## Features

- Interactive GUI for visualizing frequency and power data.
- Real-time data updates for accurate spectrum analysis.
- Select and remove serial ports for data input.
- Parameter display for reference level, attenuation, sweep time, resolution bandwidth, video bandwidth, and operating mode.
- Frequency-related information like center frequency, frequency division, and span.
- Compatible with various serial port devices providing suitable data format.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python libraries (install using `pip install -r requirements.txt`):
  - Tkinter
  - PIL (Python Imaging Library)
  - Matplotlib

### Installation and Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/spectrum-analyzer-gui.git
   cd spectrum-analyzer-gui
2. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
3. Run the GUI application:

   ```bash
   python window.py
Use the GUI to select a serial port, visualize spectrum data, and explore the provided features.

Arduino Test Script
The repository also includes a sample Arduino script (in Serial_test folder) to simulate data output. You can upload this script to an Arduino board to send simulated frequency and power data to the GUI. Make sure you connect the Arduino to your computer and select the appropriate serial port in the GUI.

Contributing
Contributions are welcome! If you find any bugs, have suggestions, or want to enhance the project, feel free to create issues or pull requests.

License
None
