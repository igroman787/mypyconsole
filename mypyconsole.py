#!/usr/bin/env python3
# -*- coding: utf_8 -*-

class MyPyConsoleItem():
	def __init__(self, cmd, func, desc):
		self.cmd = cmd
		self.func = func
		self.desc = desc
	#end define
#end class

class MyPyConsole():
	def __init__(self):
		self.name = ""
		self.unknownCmd = "Unknown command"
		self.helloText = "Welcome to the console. Enter 'help' to display the help menu."
		self.menuItems = list()
		self.AddItem("help", self.Help, "print help text")
	#end define

	def AddItem(self, cmd, func, desc):
		item = MyPyConsoleItem(cmd, func, desc)
		self.menuItems.append(item)
	#end define

	def UserWorker(self):
		result = input(bcolors.OKGREEN + self.name + "> " + bcolors.ENDC)
		if len(result) == 0:
			result = None
		return result
	#end define

	def GetCmdFromUser(self):
		cmd = self.UserWorker()
		for item in self.menuItems:
			if cmd == item.cmd:
				item.func()
				return
		print(self.unknownCmd)
	#end define

	def Help(self):
		indexList = list()
		for item in self.menuItems:
			index = len(item.cmd)
			indexList.append(index)
		index = max(indexList) + 1
		for item in self.menuItems:
			cmd = item.cmd.ljust(index)
			print(cmd, item.desc)
	#end define

	def Run(self):
		print(self.helloText)
		while True:
			self.GetCmdFromUser()
	#end define
#end class
