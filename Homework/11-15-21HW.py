# Create ToDo List App where you can add/delete/view all tasks

# create display menu to choose one of the options
def menu():   
    print("\nPress 1 to add task.\nPress 2 to delete task.\nPress 3 to view all tasks.\nPress q to quit.\n")

task_list = []
menu()


def view_tasks():
    for i in range(0,len(task_list)):
        task = task_list[i]
        print(f"{i + 1} - {task['name']} - {task['priority']}")


while True:
    choice = input("Type in the option: ")

    if choice == "1":
        name = input("name the task you want to add: ")
        priority = input("Choose priority high, medium, or low: ")
        task = {"name":name , "priority":priority}
        task_list.append(task)
    
    elif choice == "2":
        view_tasks()
        delete = int(input("Enter in task number you want to delete: " ))
        del task_list[delete - 1]

    elif choice == "3":
        if task_list == []:
            print("You have no tasks")
            continue
        else:
            view_tasks()
    
    elif choice == "q":
            break
    
    else:
        print("Error, choose another option")

print("Thank you for using the Todo List App!")