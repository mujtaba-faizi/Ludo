tasks=[]

def create():
    name = input("Enter Task name: ")
    option = input("Do you wanna add the task at some index (y/n)? or simply at the end: ")
    if option=='y':
        show()
        index = int(input("Enter the index: "))
        tasks.insert(index,{"name": name, "status": "incomplete"})
    else:
        tasks.append({ "name": name,"status": "incomplete"})
        #default status is incomplete ; data-structure used is dictionaries within list

def show():
    for count, t in enumerate(tasks):
        print("Task Index :",count, "\t\tTask name :",t["name"], "\t\tTask status :",t["status"])

def update():
    show()
    index=int(("Enter the task index for the task you want to update : "))
    option=input("Do you want to change the name? (y/n) ")
    if option == 'y':
        name=input("Enter new name : ")
        tasks[index]["name"] = name
    if tasks[index]["status"] == "incomplete":
        option=input("Do you want to change the status to completed? (y/n) ")
        if option == 'y':
            tasks[index]["status"] = "completed"

def delete():
    show()
    index = input("Enter the task index for the task you want to delete : ")
    del tasks[int(index)]

while True:
    option = int(input("1. Create a Task\n2. List tasks\n3. Update a Task\n4. Delete a Task \n0. Exit Program\n"))
    if option==1:
        create()
    elif option==2:
        show()
    elif option==3:
        update()
    elif option==4:
        delete()
    elif option==0:
        break