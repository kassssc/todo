#!/usr/bin/env python3
import json
import sys
import os

def main():

	# define constants
	DATA_FILE = "todo_data.json" # Name of json file to store data
	JSON_KEY = "todo_list" # key to access todo list in json file
	USAGE_TEXT = (
					"usage: todo.py <mode> [opt_arg]\n\n"
					"modes:\n"
					" a, add\t\tadd a new task\n"
					" a+, add+\tadd multiple tasks\n"
					" ls, list\tadd a new task\n"
					" del, delete\tdelete an existing task\n\n"
					"opt_arg:\n"
					" a, add\t\ttask to add (must be quoted if contains spaces)\n"
					" del, delete\tindex of task to be deleted\n"
				 )

	# Print usage documentation if no arguments given
	if 1 == len(sys.argv):
		print(USAGE_TEXT)
		sys.exit()

	# Create the file to store data if it doesn't exist, load it with empty data
	if not os.path.exists(DATA_FILE):
		with open(DATA_FILE, 'w') as data_file:
			json.dump({ JSON_KEY: [] }, data_file)

	# load tasks stored previously
	with open(DATA_FILE, 'r') as data_file:
		json_data = json.load(data_file)
	todo_list = json_data['todo_list']

	# First argument will specify mode
	mode = sys.argv[1]

	if len(sys.argv) == 3:
		opt_arg = sys.argv[2]
	elif len(sys.argv) > 3:
		opt_args = sys.argv[3:]
	else:
		opt_arg = None

	if mode == 'a' or mode == "add":
		if opt_arg:
			todo_list.append(opt_arg)
		else:
			new_task = input("Enter the task to add: ")
			# Adds to todo list only if not empty
			if new_task:
				todo_list.append(new_task)

	elif mode == 'a+' or mode == "add+":
		print("Adding multiple tasks, hit enter without any input when done")
		while True:
			new_task = input("Enter the task: ")
			# Breaks loop when empty string entered
			if not new_task:
				break
			todo_list.append(new_task)

	elif mode == 'ls' or mode == "list":
		if len(todo_list) == 0:
			print("Nothing on the todo list right now")
		else:
			print("Things to do:")
			for task in todo_list:
				print(' - ' + task)

	elif mode == 'del' or mode == "delete":

		if opt_arg:
			del_index = int(opt_arg)

		else:
			print("-1 : Cancel Deleting")
			for index, task in enumerate(todo_list):
				print(' ' + str(index) + ' : ' + task)
			del_index = int(input("Enter the id of task to be deleted: "))

		if del_index in range(len(todo_list)):
			del todo_list[del_index]

	# Any other argument will trigger usage text to be printed
	else:
		print(USAGE_TEXT)

	# save tasks to json file
	with open(DATA_FILE, 'w') as data_file:
		json.dump({ JSON_KEY: todo_list }, data_file)
	sys.exit()

if __name__ == '__main__': main()

