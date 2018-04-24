# todo
Simple CLI todo list app for interview at CODIUM
Kass Chupongstimun
24/04/2018

USAGE: todo.py <mode> [opt_arg]

modes:
    a, add        add a new task
      [opt_arg]   task to add (must be quoted if contains spaces)
    a+, add+      add multiple tasks
    ls, list      list all tasks
    del, delete   delete an existing task
      [opt_arg]   list index of task or the task string itself to be deleted
      
OTHER USAGE EXAMPLES: todo.py add [<task_to_add>]
                      todo.py del [<task_to_delete>]
