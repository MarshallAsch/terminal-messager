#!/usr/bin/python
import shlex, subprocess, time, thread

def setTarget(name):
	if name == "name":
		return "1111111"   #change names and numbers 
	elif name == "name":
		return "111111"
	else:
		return "-1"
	


def start():
	#get the name or person to text
	while num != "-1":
		target = raw_input("enter the name: ")
		num = setTarget(target)


def sendText(num, msg):
	cmd = ["osascript", "sendPy.scpt", num, msg]
	subprocess.call(cmd, shell=False)



def displayLog():
	oldLine = ""

	while True:
		convLog = open("conv.log", "r")
		newLine = convLog.readline()
		if newLine != oldLine:
			print newLine.rstrip()
			oldLine = newLine
		time.sleep(0.2)


def enterMessage(num):
	while True:
		message = raw_input()
		sendText(num, message)



def start():
	thread.start_new_thread(displayLog, ())
	target = raw_input("enter the name: ")
	num = setTarget(target)

	if num == "-1":
		return

	enterMessage(num)

start()

