# -*- coding: utf-8 -*-

print "Welcome to the TODO task management program."

todo_dict = {}

while True:
    task = raw_input("Please enter a TODO task: ")
    status = raw_input("Was the task completed yet? (yes/no) ")
    print "Your task is: " + task

    if status == "yes":
        todo_dict[task] = True  # this is how we add a key-value pair into a dict
    else:
        todo_dict[task] = False

    new = raw_input("Would you like to enter new task? (yes/no) ")

    if new == "no":
        break

print "All tasks: %s" % todo_dict


with open("todo.txt", "w+") as todo_file:
    print "completed tasks:"
    todo_file.write("completed tasks:\n")
    for item in todo_dict:
        if todo_dict.get(item) is True:
            print "- " + item
            todo_file.write("- " + item + "\n")
    todo_file.write("\n")

    print "Incomplete tasks:"
    todo_file.write("incomplete tasks:\n")
    for item in todo_dict:
            if todo_dict.get(item) is False:
                print "- " + item
                todo_file.write("- " + item + "\n")


print "END"