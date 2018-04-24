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

	global DATA_FILE, TODO_DATA

	# define constants
	DATA_FILE = "todo_data.json" # Name of json file to store data
	TODO_DATA = "todo_list" # key to access todo list in json dictionary
	USAGE_TEXT = (
					"USAGE: todo.py <mode> [opt_arg]\n"
					"\nmodes:\n"
					" a, add\t\tadd a new task\n"
					"  [opt_arg]:\ttask to add (must be quoted if contains spaces)\n"
					" a+, add+\tadd multiple tasks\n"
					" ls, list\tlist all tasks\n"
					" del, delete\tdelete an existing task\n"
					"   [opt_arg]:\tlist index of task or the task string itself to be deleted\n"
				 )

	# Print usage documentation and exits if no arguments given
	if 1 == len(sys.argv):
		print(USAGE_TEXT)
		sys.exit()

	# Load data from storage json file
	todo_list = load_data()

	# First argument will specify mode
	mode = sys.argv[1]
	# Extract program optional argument (if provided)
	if len(sys.argv) >= 3:
		opt_arg = sys.argv[2]
	else:
		opt_arg = None

	# Add task mode
	if mode == 'a' or mode == "add":
		# use optional argument if provided, else prompt for input
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
		# use optional argument if provided, else prompt for input
		if opt_arg is not None:
			user_input = opt_arg
		else:
			for index, task in enumerate(todo_list):
				print(' ' + str(index) + ' : ' + task)
			print(" * Hit enter without any input to cancel")
			user_input = input("Enter the id of the task or the task itself to be deleted: ")

		delete_from_list(user_input, todo_list)

	# Any other argument will trigger usage text to be printed
	else:
		print(USAGE_TEXT)

	# Save data to json file for storage
	save_data(todo_list)

	#**************
	# END PROGRAM
	#**************

def delete_from_list(user_input, todo_list):
	'''
	If user_input is parsable an integer,
		If the index is in range, deletes the task at that index
		otherwise will return, doing nothing.
	If user_input is a string (not parsable as integer),
		if it is an empty string, return doing nothing
		If that string doesn't match any task in the list, return doing nothing.
		If that string exists matches a task in that list, remove that task
		If multiple instances of the same task exists, only the first is deleted.
	'''

	try:
		index = int(user_input) # Throws ValueError if not parsable to int
		if index in range(len(todo_list)):
			print("Task \"" + todo_list[index] + "\" deleted")
			del todo_list[index]
		else:
			print("Invalid index provided, nothing deleted")
		return

	# Value Error thrown means user entered a non-integer input
	except ValueError:
		# Check for empty string
		if user_input == "":
			print("Delete cancelled")
			return

		# If it exists in the list, loop through and get the corresponding index
		for task in todo_list:
			if user_input.lower() == task.lower(): # ignore case
				del todo_list[todo_list.index(task)]
				print("Task \"" + task + "\" deleted")
				return

		# Reached only if task provided doesn't match any in the list
		print("Task \"" + user_input + "\" doesn't exist in the list")

def load_data():
	'''
	Handles cases where the data file already exists and doesn't exist
	Returns the previously stored data in the form of a list.
	'''
	# If the data file doesn't exist, create it and load it with an empty list
	if not os.path.exists(DATA_FILE):
		with open(DATA_FILE, 'w') as data_file:
			json.dump({ TODO_DATA: [] }, data_file)

	# load tasks stored previously
	with open(DATA_FILE, 'r') as data_file:
		json_data = json.load(data_file)

	return json_data[TODO_DATA]

def save_data(todo_list):
	'''Stores the data in the list to the json file'''

	with open(DATA_FILE, 'w') as data_file:
		json.dump({ TODO_DATA: todo_list }, data_file)

# Program Entry Point
if __name__ == '__main__': main()
