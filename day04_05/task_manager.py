def show_menu():
    print("\n--- Task manager ---")
    print("1. add task")
    print("2. view tasks")
    print("3. mark task as done")
    print("4. delete task")  
    print("5. exit")

def add_task(tasks):
    title =input("Enter task title: ")
    task = {
        "title": title,
           "done": False
    }
    tasks.append(task)
    print("task added.")

def view_tasks(tasks):
    if not tasks:
        print("no tasks yet.")
        return
    
    for index, task in enumerate(tasks):
        status ="yes" if task["done"] else "no"
        print (f"{index + 1},[{status}] {task['title']}")

def mark_task_done(tasks):
    view_tasks(tasks)
    
    if not tasks:
        return
    
    Choice = input("Enter task number to mark done: ")

    if not Choice.isdigit():
        print ("invalid input")
        return
    
    index = int(Choice) - 1

    if index < 0 or index >= len(tasks):
        print ("task not found.")
        return
    
    tasks[index]["done"] = True
    print("task marked as done.")

def del_task(tasks):
    view_tasks(tasks)
    
    if not tasks:
        return
    
    Choice = input("Enter task number to delete: ")

    if not Choice.isdigit():
        print ("invalid input")
        return
    
    index = int(Choice) - 1

    if index < 0 or index >= len(tasks):
        print ("task not found.")
        return
    
    tasks.pop(index)
    print("task deleted.")
   


def main():
    tasks = []
    while True :
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            del_task(tasks)
        elif choice =="5":
            print ("Goodbye.")
            break
        else:
            print("Invalid options.")

main()