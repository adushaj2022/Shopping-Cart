from ItemDushaj import ItemDushaj

##Anthony Dushaj



##Purpose: To allow the user to virtually shop through a grocery store, by their prompts

##Inputs: To add an item, the user must enter the name, quantity, and unitprice per item. The user can input different choices into a menu to alter or view their cart

##Outputs: Total number of items, determining whether the list is empty, total cost of items in the list, all the items in the cart




def main():
    askUserFile = input("Please enter filename, thank you! : ")
    #This line demonstrates initial data being gained, by inserting the file parameter into the function which returns the list of items
    ListOfItems = getList(askUserFile)

    menuPrint = """
        1. Add an item to the list
        2. Delete an item from the list(*)
        3. Print each item in the list
        4. Search for a user-specified item in the list
        5. Count the total number of items in the list
        6. Total the cost of the items in the list
        7. Determine whether the list is empty
        8. Clear the list
        0. Quit
        """
    print(menuPrint)
    
    userEnter = input("Please enter one in one of the following choices: ")
    while(userEnter == "1")or(userEnter == "2")or(userEnter == "3")or(userEnter == "4")or(userEnter == "5")or(userEnter == "6")or(userEnter == "7")or(userEnter == "8"):

            if userEnter == "1":
                #This call a function to append a item, to the previous list, which will be put into the parameter
                Choice1 = appendValue1(ListOfItems)
                print("Quantity      Name     UnitPrice")
                #We will print the updated shopping cart
                Choice1_2 = printItem3(ListOfItems)
                if Choice1_2 == None:
                    Choice1_2 = "  "
                print(Choice1_2)
                
            elif userEnter == "3":
                #This will call the function to print each item in the list (ListOfItems)
                print("Quantity      Name     UnitPrice")
                Choice3 = printItem3(ListOfItems)
                if Choice3 == None:
                    Choice3 = "  "
                print(Choice3)
                
            elif userEnter == "4":
                #This will call the function to prompt the user for a search, and return a result
                Choice4 = findSpecific4(ListOfItems)
                if Choice4 == None:
                     Choice4 = "  "
                print(Choice4)
                
            elif userEnter == "5":
                #This will call the  function to return the total items in the list, by accepting a parameter of the list
                Choice5 = findTotalQuant5(ListOfItems)
                print("The total number of items in your cart is: ", Choice5)
            elif userEnter == "6":
                #This will call the function to return the total cost of all items in the list, and will format the price into a real life money scenario
                Choice6 = findUnitPrice6(ListOfItems)
                print("The total unit price is ${0:0.2f} ".format(Choice6))
            elif userEnter == "7":
                #This will call the function to accept the list of the items and will determine by its length, if its empty or not
                Choice7 = determineSize7(ListOfItems)
                print(Choice7)
            elif userEnter == "8":
                #This will call the function to clear the list, and tell the user that it cleared the list
                Choice8 = clearList8(ListOfItems)
                print(Choice8)
                
            print(menuPrint)
            userEnter = input("Please enter one in one of the following choices: ")
                
#This function accepts a parameter of a filename
#It will return the items in the file as a list
def getList(openFilename):
        openFile = open(openFilename, 'r')
        
        newList = []
        line_limit = int(openFile.readline())

        for line in range(line_limit):
            
            userName = openFile.readline().strip()
            userQuantity = int(openFile.readline())
            userPrice = float(openFile.readline())
            
            object_1 = ItemDushaj(userQuantity, userName, userPrice)
            newList.append(object_1)
            
        return newList
#This function accepts the paramter of a list
#It will prompt the user to append a item to the list, and returns no value
def appendValue1(list_value):
    askName = input("Please enter the name: ")
    askQuant = int(input("Please enter the quantity: "))
    askPrice = float(input("Please enter the unitprice: "))
    object_create = ItemDushaj(askQuant, askName, askPrice)
    list_value.append(object_create)
    print("We have added: ", askName)


#This function accepts the parameter of a list
#It will print each item in the list
def printItem3(listofVals):
    for item in listofVals:
        print(item)


   
#This function will accept the parameter of a list
#This function will prompt the user to find a specific item name in the list
#This function will not return anything
def findSpecific4(value_lister):
    searchItem = input("What is the item name: ")
    foundItem = 0
    for i in range(len(value_lister)):
        if searchItem == value_lister[i].getName():
            foundItem += 1    
            print("Yes you have", value_lister[i].getQuantity(), searchItem, "at ", "${0:0.2f}".format(value_lister[i].getUnitPrice()), " each")
    #foundItem will indicate if a word was found, if it was not its value will remain 0 and print out a message
    if foundItem == 0:
        print("Your item ", searchItem," was not found!")

        


#This function will accept the parameter of a list
#This function will return the total amount of items in list
def findTotalQuant5(listsValues):
    totalquant = 0
    for i in range(len(listsValues)):
        totalquant += (listsValues[i].getQuantity())



    return totalquant

#This function will accept the parameter of a list
#This function will return the total price of all the items in the list
def findUnitPrice6(listcount):
    listprice = 0
    for i in range(len(listcount)):
        #OneItems price equals unitprice * quantity
        listprice += (listcount[i].getUnitPrice() * listcount[i].getQuantity())


    return listprice
#This function accepts the parameter of a list
#This function will return if the list is empty or not
def determineSize7(determineList):
    if len(determineList)> 0:
        listsize = "The list is not empty"
    else:
        listsize = "The list is empty currently"

    return listsize

#This function accepts the paramter of a list
#This function will clear the list return a string that awares the user of the list being cleared
def clearList8(clear_List):
    while len(clear_List) > 0:
        clear_List[:] = []
        answerStatement = "The list is now clear"
    return answerStatement

        
        

main()
        
    
    


    
            
           
        
            
            
        
            
             

            

   
    
