#!/usr/bin/env python3
# -*- coding: utf_8 -*-

import os
import sys
import readline

class MyPyConsoleItem():
	def __init__(self, cmd, func, desc):
		self.cmd = cmd
		self.func = func
		self.desc = desc
	#end define
#end class

class MyPyConsole():
	RED = '\033[31m'
	GREEN = '\033[92m'
	ENDC = '\033[0m'

	def __init__(self):
		self.debug = False
		self.name = "console"
		self.color = self.GREEN
		self.unknown_cmd = "Unknown command"
		self.hello_text = "Welcome to the console. Enter 'help' to display the help menu."
		self.startFunction = None
		self.start_function = None
		self.menu_items = list()
		self.add_item("help", self.help, "Print help text")
		self.add_item("clear", self.clear, "Clear console")
		self.add_item("exit", self.exit, "Exit from application")
		readline.parse_and_bind("tab: complete")
		readline.set_completer(self.readline_completer)
	#end define

	def readline_completer(self, text, state):
		commands = [item.cmd for item in self.menu_items if item.cmd.startswith(text)]
		if state < len(commands):
			return commands[state]
		return None
	#end define
	
	def AddItem(self, cmd, func, desc):
		self.add_item(cmd, func, desc)
	#end define

	def add_item(self, cmd, func, desc):
		item = MyPyConsoleItem(cmd, func, desc)
		self.menu_items.append(item)
	#end define

	def user_worker(self):
		try:
			result = input(self.color + self.name + "> " + self.ENDC)
		except KeyboardInterrupt:
			self.exit()
		except EOFError:
			self.exit()
		return result
	#end define

	def get_cmd_from_user(self):
		result = self.user_worker()
		result_list = result.split(' ')
		result_list = list(filter(None, result_list))
		cmd = self.get_item_from_list(result_list, 0)
		args = result_list[1:]
		for item in self.menu_items:
			if cmd == item.cmd:
				if self.debug == True:
					item.func(args)
				else:
					self._try(item.func, args)
				print()
				return
		print(self.unknown_cmd)
	#end define
	
	def _try(self, func, args):
		try:
			func(args)
		except Exception as err:
			print("{RED}Error: {err}{ENDC}".format(RED=self.RED, ENDC=self.ENDC, err=err))
	#end define

	def help(self, args=None):
		indexList = list()
		for item in self.menu_items:
			index = len(item.cmd)
			indexList.append(index)
		index = max(indexList) + 1
		for item in self.menu_items:
			cmd = item.cmd.ljust(index)
			print(cmd, item.desc)
	#end define

	def clear(self, args=None):
		os.system("clear")
	#end define

	def exit(self, args=None):
		print("Bye.")
		sys.exit()
	#end define
	
	def Run(self):
		self.start_function = self.startFunction
		self.run()
	#end define

	def run(self):
		print(self.hello_text)
		if self.start_function:
			self.start_function()
		while True:
			self.get_cmd_from_user()
	#end define

	def get_item_from_list(self, data, index):
		try:
			return data[index]
		except: pass
	#end define
#end class
