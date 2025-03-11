import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up serial connection (Change "COM3" to your port on Windows or "/dev/ttyUSB0" on Linux/Mac)
ser = serial.Serial('COM3', 9600, timeout=1)

# Initialize the figure
fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot([], [], 'b-', lw=2)

def init():
    ax.set_xlim(0, 100)  # Show last 100 points
    ax.set_ylim(0, 1023)  # Arduino's 10-bit ADC range (0-1023)
    ax.set_xlabel("Time")
    ax.set_ylabel("Sensor Value")
    return line,

def update(frame):
    try:
        # Read Serial Data
        data = ser.readline().decode().strip()
        if data:
            value = int(data)
            x_data.append(len(x_data))  # Time axis (frame count)
            y_data.append(value)
            
            # Keep only the last 100 points
            if len(x_data) > 100:
                x_data.pop(0)
                y_data.pop(0)

            line.set_data(x_data, y_data)
    except:
        pass
    return line,

ani = animation.FuncAnimation(fig, update, init_func=init, blit=False, interval=50)

plt.title("Real-Time Sensor Data Plot")
plt.show()

ser.close()
