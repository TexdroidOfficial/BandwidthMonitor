# Bandwidth Monitor 🖥️📶

This is a simple script developed as a personal project to monitor network bandwidth usage (sent, received, and total) for a specified duration.

## Description 📜

The script initiates a GUI built with `customtkinter` upon execution. Once the GUI window is closed, the script starts monitoring network traffic using `psutil`. After the monitoring period (default is 15 seconds), it displays real-time data on the amount of data received, sent, and the total data transferred, along with the average rates in the terminal. The script performs the following operations:

1. **GUI Initiation:** Opens a simple GUI window built with `customtkinter`. Upon closing this window, the monitoring process starts.
2. **Network Monitoring:** Monitors the network traffic (sent, received, and total) for a predefined duration (default 15 seconds) using the `psutil` library.
3. **Data Display:** After the monitoring period, displays the collected data in the terminal, including the total data received, sent, and the total data transferred, along with average rates.

## How to use 🚀

1. **Prerequisites:** Make sure you have Python, `customtkinter`, and `psutil` libraries installed on your system. If these libraries are not installed, install them using pip:

   ```bash
   pip install customtkinter psutil
   ```
3. Navigate to the script directory: Open the command line or terminal and navigate to the directory where the script file is located. You can use the `cd` (change directory) command for this. For example, if the script is in the "MyScripts" folder, you would use: `cd MyScripts`.
4. Script execution: Once you are in the correct directory, execute the script from the command line using the following command:

   ```bash
    python bandwidthMonitor.py
    ```
5. Monitoring: The script will first open a GUI window built with `customtkinter`. Close the GUI window to start the network monitoring. The script will monitor the network for 15 seconds (or the specified duration) using `psutil` and then display the results in the terminal.

## Screenshots 📸

![2025-03-30 17-47-33 start=1 length=23 fps=30](https://github.com/user-attachments/assets/f6b4eff3-c93e-4771-ad1b-9fb49b3d47e7)

## License 📄

This project is licensed under the [MIT License](LICENSE).

##
Made with ❤️ by Texdroid
