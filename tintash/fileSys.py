import os

def create(mode):
    name = input("Enter File name: ")
    f = open(name+".txt", mode)
    return f

def show():
    f = create("r")
    content = f.read()
    print(content)
    f.close()

def update():
    option = input("Do you wanna overwrite the file (y/n)? or append it? ")
    if option =='y':
        f = create("w+")
    else:
        f = create("a+")
    content = input("Enter the content you want to add in the file : ")
    f.write(content)
    while True:
        option = input("Do you wanna add a new line (y/n)? ")
        if option!='y':
            break
        content = input("Enter the content you want to add in the file : ")
        f.write("\n"+content)
    f.close()

def delete():
    name = input("Enter the file name you want to delete : ")
    if os.path.exists(name+".txt"):
        os.remove(name+".txt")
    else:
        print("The file does not exist")

def search():
    check=0
    content = input("Enter the content to check : ")
    f = create("r")
    for line in f.readlines():
        if content in line:
            print("The content exists in the file")
            check=1
            break
    if check==0:
        print("The content does not exist in the file")

def replace():
    word = input("Enter the word to replace : ")
    rep = input("Enter the word to replace with : ")
    f = create("r+")
    content = f.read()
    new_content = content.replace(word, rep)
    f.truncate(0)
    f.write(new_content)
    print("Replaced!!")
    f.close()

while True:
    option = int(input("1. Create a File\n2. Show File Content\n3. Update a File\n4. Delete a File \n5. Search content from a File "
                       "\n6. Replace all \n0. Exit Program\n"))
    if option==1:
        f = create("w+")
        f.close()
    elif option==2:
        show()
    elif option==3:
        update()
    elif option==4:
        delete()
    elif option==5:
        search()
    elif option==6:
        replace()
    elif option==0:
        break