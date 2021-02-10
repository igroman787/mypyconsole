#!/usr/bin/env python3
# -*- coding: utf_8 -*-

import os
import sys
import tty
import termios



x = 0
pos = 0

class Keyboard:
	enter = b'\n'
	esc = b'\x1b'
	mov = b'\x1b['
	left = b'\x1b[D'
	rigth = b'\x1b[C'
	top = b'\x1b[A'
	bottom = b'\x1b[B'
	moving = [left, rigth, top, bottom]
	backspace = b'\x7f'
	ctrlD = b'\x04'
	sru1 = b'\xd0'
	sru2 = b'\xd1'
	sru = [sru1, sru2]
#end class

def ReadInput():
	buff = b''
	while True:
		buff += sys.stdin.buffer.read(1)
		if buff == Keyboard.esc:
			continue
		elif buff == Keyboard.mov:
			continue
		elif buff in Keyboard.sru:
			continue
		else:
			break
	#end while
	return buff
#end define

def GetTerminalSize():
	data = os.get_terminal_size()
	x = data.columns
	y = data.lines
	return x, y
#end define

def LineReset():
	global x
	text = b' ' * x
	sys.stdout.buffer.write(b'\r' + text)
#end define

def ScreenPrint(textList):
	dataList = textList.copy()
	dataList.insert(pos, b'\x1b7')
	data = b''.join(dataList)
	LineReset()
	sys.stdout.buffer.write(b'\r' + data +  b'\x1b8')
	sys.stdout.flush()
#end define

def Work():
	global pos, x
	x, y = GetTerminalSize()
	textList = list()
	pos = 0
	while True:
		r = ReadInput()
		if r in Keyboard.enter:
			textList.clear()
			pos = 0
		elif r == Keyboard.left:
			if pos > 0:
				pos -= 1
		elif r == Keyboard.rigth:
			if pos < len(textList):
				pos += 1
		elif r == Keyboard.backspace:
			if pos > 0:
				textList.pop(pos-1)
				pos -= 1
		else:
			textList.insert(pos, r)
			pos += 1
		ScreenPrint(textList)
	#end while
#end define

def Main():
	try:
		# disable readline
		old_settings = termios.tcgetattr(sys.stdin)
		tty.setcbreak(sys.stdin.fileno())
		Work()
	except Exception as err:
		print(err)
	finally:
		# enable readline
		termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
#end define

# while True:
# 	r = ReadInput()
# 	print(r)
# #end while

if __name__ == "__main__":
	Main()
#end if

