from pyautogui import *
import time
import keyboard
import win32api, win32con

# settings icon position	-> x: 1435 y: 964
# speed location 			-> x: 1404 y: 867
# 2x location				-> x: 1345 y: 901
# next video icon			-> x: 792 y: 576
ICON_LOC_POS = (1435, 964)
SPEED_LOC_POS = (1404, 867)
LOC_2X_POS = (1345, 901)
LOC_SKIP_ICON = (792,576)
def click(*args):
	win32api.SetCursorPos(*args)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(0.01)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def skip_video(*args):
	click(*args)
	# MOVE AWAY CURSOR TO CLOSE INTERFACE
	moveTo(1700,560)
def change_speed_pixelwise():
	# HOVER OVER VIDEO TO GET VISIBLE VIDEO ELEMENTS
	moveTo(800,560)
	sleep(0.1)
	# CHANGE VIDEO SPEED
	click(ICON_LOC_POS)
	time.sleep(0.15)
	click(SPEED_LOC_POS)
	time.sleep(0.15)
	click(LOC_2X_POS)
	time.sleep(0.15)
	# CLOSE SETTINGS PANEL
	click(ICON_LOC_POS)
	# MOVE AWAY CURSOR TO CLOSE INTERFACE
	moveTo(1700,560)
def main():
	while keyboard.is_pressed('q') == False:
		if(keyboard.is_pressed('e') == True):
			change_speed_pixelwise()
		elif keyboard.is_pressed('w'):
			skip_video(LOC_SKIP_ICON)
		time.sleep(0.5) # reduces power consume
if __name__ == "__main__":
	main()