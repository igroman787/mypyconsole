#!/usr/bin/env python3
# -*- coding: utf_8 -*-

import os
import sys

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
		self.name = ""
		self.unknownCmd = "Unknown command"
		self.helloText = "Welcome to the console. Enter 'help' to display the help menu."
		self.menuItems = list()
		self.AddItem("help", self.Help, "Print help text")
		self.AddItem("clear", self.Clear, "Clear console")
		self.AddItem("exit", self.Exit, "Exit from application")
	#end define

	def AddItem(self, cmd, func, desc):
		item = MyPyConsoleItem(cmd, func, desc)
		self.menuItems.append(item)
	#end define

	def UserWorker(self):
		try:
			result = input(self.GREEN + self.name + "> " + self.ENDC)
		except KeyboardInterrupt:
			self.Exit()
		except EOFError:
			self.Exit()
		return result
	#end define

	def GetCmdFromUser(self):
		result = self.UserWorker()
		resultList = result.split(' ')
		cmd = resultList[0]
		args = resultList[1:]
		for item in self.menuItems:
			if cmd == item.cmd:
				#try:
				item.func(args)
				#except Exception as err:
				#	print("{RED}Error: {err}{ENDC}".format(RED=self.RED, ENDC=self.ENDC, err=err))
				print()
				return
		print(self.unknownCmd)
	#end define

	def Help(self, args=None):
		indexList = list()
		for item in self.menuItems:
			index = len(item.cmd)
			indexList.append(index)
		index = max(indexList) + 1
		for item in self.menuItems:
			cmd = item.cmd.ljust(index)
			print(cmd, item.desc)
	#end define

	def Clear(self, args=None):
		os.system("clear")
	#end define

	def Exit(self, args=None):
		print("Bye.")
		sys.exit()
	#end define

	def Run(self):
		print(self.helloText)
		while True:
			self.GetCmdFromUser()
	#end define
#end class
