import pyautogui as ptg
import json
import sys
import time
import random as rand

if len(sys.argv) != 2:
    print("Usage: python script.py <input_file.json>")
    sys.exit(1)

input_file = sys.argv[1]

def load_data(file):
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: File '{file}' is not a valid JSON file.")
        sys.exit(1)

points = load_data(input_file)

if not points:
    print("No points found in the file.")
    sys.exit(1)

print("Monitoring pixel colors. Press Ctrl+C to stop.")

try:
    while True:
        for point in points:
            x, y = point["x"], point["y"]
            stored_color = tuple(point["color"].values())

            current_color = ptg.screenshot().getpixel((x, y))

            if current_color != stored_color:
                print(f"Color change detected at ({x}, {y}): {current_color} != {stored_color}")
                ptg.click(x, y)
            time.sleep(rand.uniform(0.1, 0.5))

except KeyboardInterrupt:
    print("Monitoring stopped.")
