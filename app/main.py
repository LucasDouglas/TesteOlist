from model.sqlmodel import ReadAll
from controller.pandacontroller import panda_connect
from model.sqlmodel import ReadAll2
from model.sqlmodel import  Create
from model.sqlmodel import Alterate
from model.sqlmodel import Delete
from model.sqlmodel import ReadName
from model.sqlmodel import ReadDescription
from model.sqlmodel import ReadCategory
from model.sqlmodel import ReadValue
from controller.pandacontroller import panda_connect


menu = input("Chose the option - 1 for Create - 2 for Alterate - 3 for Delete - 4 Read - 5 Execute CSV categories for Categorias database")

if menu == "1":
    var1 = input("type the name:")
    var2 = input("type the description:")
    var3 = float(input("type value:"))
    var4 = int(input("type the Id of the category:"))
    try:
        Create(var1, var2, var3, var4)
    except Exception as exp:
        print("error try again")
    else:
        print("sucess")

elif menu == "2":
    var5 = int(input("Choose the ID to alterate:"))
    var1 = input("type the name:")
    var2 = input("type the description:")
    var3 = float(input("type value:"))
    var4 = int(input("type the Id of the category:"))
    try:
        Alterate(var1, var2, var3, var4, var5)
    except Exception as exp:
        print("error try again")
    else:
        print("sucess")


elif menu == "3":
    var1 = int(input("Choose the ID the delete:"))
    try:
        Delete(var1)
    except Exception as exp:
        print("error try again")
    else:
        print("sucess")


elif menu == "4":
    varRead = (input("Choose the option to search - 1 for search all - 2 for search by name - 3 for search by description - 4 for search by value - 5 for search by category"))
    if varRead == "1":
        try:
            ReadAll()
        except Exception as exp:
            print("error try again")   
        else:
            print("sucess") 

    elif varRead == "2":
        var1 = input("Type the name to search:")
        try:
            ReadName(var1)
        except Exception as exp:    
            print("error try again")
        else:
            print("sucess")

    elif varRead == "3":
        var1 = input("Type the description to search:")
        try:
            ReadDescription(var1)
        except Exception as exp:
            print("error try again")
        else:
            print("sucess")

    elif varRead == "4":
        var1 = float(input("Type the value to search:"))
        try:
            ReadValue(var1)
        except Exception as exp:
            print("error try again")   
        else:
            print("sucess") 

    elif varRead == "5":
        var1 = int(input("Type the category to search:"))
        try:
            ReadCategory(var1)
        except Exception as exp:
            print("error try again")    
        else:
            print("sucess")
    else:
        print("The option selection was wrong try again")       

elif menu == "5":
    try:
        panda_connect()
    except Exception as exp:
        print("error to execute panda")
    else:
        print("sucess")

else:
    print("The menu selection was wrong try again")



