todo_tasks = {}

while True:
    task_to_add = input("Vnesi task: ")
    task_done = input ("Ali je task končan [da/ne]: ")


    todo_tasks[task_to_add] = True if task_done == "da" else False

    add_another = input ("Želiš dodati še en task [da/ne]: ")
    if add_another != "da":
        break


for task, done in todo_tasks.items():
    print (f" - {task.capitalize()} ..... {'DONE' if done else 'not done'}")
