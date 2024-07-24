def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Exit")

def view_task(tasks):
    if not tasks:
        print("\n Your To- do- List is Empty")

    else:
        for idx, tasks in enumerate(tasks,start=1):
            print("\n Your To- do- List are: ")
            print(f"{idx}. {tasks}")

def add_task(tasks):
    task=input("Enter a Task: ")
    tasks.append(task)
    print(f"The task {tasks} added.")

def remove_task(tasks):
    view_task(tasks)
    task_num=int(input("Enter the serial Number of the task: "))
    if 1 <= task_num <= len(tasks):
        remo_task =tasks.pop(task_num-1)
        print(f"The task {remo_task} is removed.")
    else:
        print("Enter a valid number")


def main():
    tasks=[]
    while True:
        display_menu()
        choice=input("Choose an option (1-4): ")
        if choice == "1":
            view_task(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Good Bye..")
            break
        else:
            print("Enter a number between (1-4)")

if __name__=="__main__":
    main()

    // tmp modify