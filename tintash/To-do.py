tasks=[]

def create():
    name = input("Enter Task name: ")
    tasks.append([name,"incomplete"])   #default status is incomplete ; data-structure used is nested list

def show():
    count=0
    for t in tasks:
        print("Task Index :",count, "\t\tTask name :",t[0], "\t\tTask status :",t[1])
        count+=1

def update():
    show()
    index=input("Enter the task index for the task you want to update : ")
    index=int(index)
    option=input("Do you want to change the name? (y/n) ")
    if option == 'y':
        name=input("Enter new name : ")
        tasks[index][0] = name
    if tasks[index][1] == "incomplete":
        option=input("Do you want to change the status to completed? (y/n) ")
        if option == 'y':
            tasks[index][1] = "completed"

def delete():
    show()
    index = input("Enter the task index for the task you want to delete : ")
    del tasks[int(index)]

for a in range(1000):
    option = input("1. Create a Task\n2. List tasks\n3. Update a Task\n4. Delete a Task \n0. Exit Program\n")
    option=int(option)
    if option==1:
        print(option)
        create()
    elif option==2:
        show()
    elif option==3:
        update()
    elif option==4:
        delete()
    elif option==0:
        break