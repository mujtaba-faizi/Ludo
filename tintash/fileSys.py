import os


def open_(mode):
    name = input("Enter File name: ")
    if os.path.exists(name + ".txt"):
        file = open(name + ".txt", mode)
        return file
    else:
        print("The file does not exist.")
        return None


def create():
    name = input("Enter File name: ")
    if os.path.exists(name + ".txt"):
        print("The file already exists.")
    else:
        file = open(name + ".txt", "w+")
        print("Created!!")
        file.close()


def show():
    file = open_("r")
    if file is not None:
        content = file.read()
        print(content)
        file.close()


def update():
    option1 = input("Do you wanna overwrite the file (y/n)? ")
    if option1 == 'y':
        file = open_("w")
    else:
        file = open_("a")
    if file is not None:
        content = input("Enter the content you want to add in the file : ")
        file.write(content)
        while True:
            option2 = input("Do you wanna add a new line (y/n)? ")
            if option2 != 'y':
                break
            content = input("Enter the content you want to add in the file : ")
            file.write("\n" + content)
        file.close()


def delete():
    name = input("Enter the file name you want to delete : ")
    if os.path.exists(name + ".txt"):
        os.remove(name + ".txt")
        print("Deleted!!")
    else:
        print("The file doesn't exist.")


def search():
    file = open_("r")
    if file is not None:
        content = input("Enter the content to check : ")
        for line in file.readlines():
            if content in line:
                print("The content exists in the file.")
                return None
        print("The content does not exist in the file.")
        file.close()


def replace():
    file = open_("r+")
    if file is not None:
        word = input("Enter the word to replace : ")
        replacing_word = input("Enter the word to replace with : ")
        for count, line in enumerate(file.readlines()):
            if count == 0:     # Firstly, all the file content needs to removed before adding the new content.
                file.truncate(0)
            new_line = line.replace(word, replacing_word)
            file.write(new_line)
        print("Replaced!!")
        file.close()


while True:
    option = input("1. Create a File\n2. Show File Content\n3. Update a File\n4. Delete a File"
                   " \n5. Search content from a File\n6. Replace all \n0. Exit Program\n")
    try:
        option = int(option)
    except ValueError:      # When the user enters anything other than an integer
        print("Please select the right option (i.e. 0-6)")
    finally:
        if option == 1:
            create()
        elif option == 2:
            show()
        elif option == 3:
            update()
        elif option == 4:
            delete()
        elif option == 5:
            search()
        elif option == 6:
            replace()
        elif option == 0:
            break
        else:
            print("Please select the right option (i.e. 0-6)")
