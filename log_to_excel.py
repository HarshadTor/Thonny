import serial
import openpyxl
from datetime import datetime

# Replace 'COM6' with your ESP32's port (Windows), or '/dev/ttyUSB0' (Mac/Linux)
ser = serial.Serial("COM6", 115200, timeout=1)

# Create or open an Excel file
wb = openpyxl.Workbook()
ws = wb.active
ws.append(["Timestamp", "Switch State"])  # Add headers

try:
    while True:
        data = ser.readline().decode("utf-8").strip()  # Read data from ESP32
        if data:
            print(f"Switch State: {data}")  # Show live data in terminal
            ws.append([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), data])  # Save to Excel
            wb.save("switch_log.xlsx")  # Save Excel file
except KeyboardInterrupt:
    print("\nLogging stopped.")
    ser.close()
    wb.save("switch_log.xlsx")  # Final save before exiting
