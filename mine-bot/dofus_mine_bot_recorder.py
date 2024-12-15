import pyautogui as ptg
import json
import sys
import keyboard as kb

if len(sys.argv) != 2:
	print("Usage: python script.py <output_file.json>")
	sys.exit(1)

output_file = sys.argv[1]

data = []

def record_pixel_data():
	try:
		x, y = ptg.position()
		color = ptg.screenshot().getpixel((x, y))
		point = {
			"x": x,
			"y": y,
			"color": {
				"r": color[0],
				"g": color[1],
				"b": color[2]
			}
		}
		data.append(point)
		with open(output_file, 'w') as file:
			json.dump(data, file, indent=4)
		print(f"Recorded: {point}")
	except Exception as e:
		print(f"Error recording data: {e}")

print("Press 'a' to record pixel data. Press 'q' to quit.")

while True:
	try:
		if kb.is_pressed('a'):
			record_pixel_data()
			kb.wait('a', suppress=True)
		elif kb.is_pressed('q'):
			print("Exiting...")
			break
	except kbInterrupt:
		print("Exiting...")
		break