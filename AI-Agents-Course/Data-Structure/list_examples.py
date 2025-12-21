## to-do list app

to_do_list = ["Buy groceries", "Clean the house", "Pay bills"]

## Adding task
to_do_list.append("Walk the dog")
to_do_list.append("Read a book")

## remove task
to_do_list.remove("Pay bills")

## checking a task in list

if "Clean the house" in to_do_list:
    print("Task found: Clean the house")

## print all tasks
print("To-Do List:")
for task in to_do_list:
    print("- " + task)

