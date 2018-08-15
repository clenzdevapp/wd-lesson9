print "Welcome to the TODO task management program."

todo_list = []

while True:
    task = raw_input("Please enter a TODO task: ")
    print "Your task is: " + task
    todo_list.append(task)  # this is how we add (append) a variable into a list

    new = raw_input("Would you like to enter new task? (yes/no) ")

    if new == "no":
        break

print "All tasks:"

for item in todo_list:
    print item

print "END"