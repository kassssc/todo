#!/usr/bin/env python3
'''
todo.py : A simple CLI to-do list program
Author: Kass Chupongstimun
Date: 24/04/2018
'''

import json
import sys
import os

def main():
	'''Main method of the CLI todo list program'''

	# define constants
	DATA_FILE = "todo_data.json" # Name of json file to store data
	TODO_LIST = "todo_list" # key to access todo list in json dictionary
	USAGE_TEXT = (
					"usage: todo.py <mode> [opt_arg]\n"
					"\nmodes:\n"
					" a, add\t\tadd a new task\n"
					"  opt_arg:\ttask to add (must be quoted if contains spaces)\n"
					" a+, add+\tadd multiple tasks\n"
					" ls, list\tlist all tasks\n"
					" del, delete\tdelete an existing task\n"
					"   opt_arg:\tindex of task to be deleted\n"
				 )

	# Print usage documentation if no arguments given
	if 1 == len(sys.argv):
		print(USAGE_TEXT)
		sys.exit()

	# If the data file doesn't exist, create it and load it with empty data
	if not os.path.exists(DATA_FILE):
		with open(DATA_FILE, 'w') as data_file:
			json.dump({ TODO_LIST: [] }, data_file)

	# load tasks stored previously
	with open(DATA_FILE, 'r') as data_file:
		json_data = json.load(data_file)
	todo_list = json_data[TODO_LIST]

	# First argument will specify mode
	mode = sys.argv[1]

	# Extract program optional argument (if provided)
	if len(sys.argv) >= 3:
		opt_arg = sys.argv[2]
	else:
		opt_arg = None

	# Add task mode
	if mode == 'a' or mode == "add":
		if opt_arg is not None:
			new_task = opt_arg
		else:
			new_task = input("Enter the task to add: ")
		# Adds to todo list only if not empty
		if new_task != "":
			todo_list.append(new_task)

	# Add multiple tasks mode
	elif mode == 'a+' or mode == "add+":
		print("Adding multiple tasks, hit enter without any input when done")
		while True:
			new_task = input("Enter the task: ")
			# Breaks loop when empty string entered
			if new_task == "":
				break
			todo_list.append(new_task)

	# List task mode
	elif mode == 'ls' or mode == "list":
		if len(todo_list) == 0:
			print("Nothing on the todo list right now")
		else:
			print("Things to do:")
			for task in todo_list:
				print(' - ' + task)

	# Delete task mode
	elif mode == 'del' or mode == "delete":
		if opt_arg is not None:
			del_index = opt_arg

		else:
			print("-1 : Cancel Deleting")
			for index, task in enumerate(todo_list):
				print(' ' + str(index) + ' : ' + task)
			del_index = input("Enter the id of task to be deleted: ")

		try:
			del_index = int(del_index) # Throws ValueError if not parsable to int
			if del_index != -1: # don't delete if user enters -1
				del todo_list[del_index] # throws IndexError if not within range
		except (IndexError, ValueError):
			print("Invalid index provided")

	# Any other argument will trigger usage text to be printed
	else:
		print(USAGE_TEXT)

	# save tasks to json file then exit
	with open(DATA_FILE, 'w') as data_file:
		json.dump({ TODO_LIST: todo_list }, data_file)
	sys.exit()

# Program Entry Point
if __name__ == '__main__': main()
