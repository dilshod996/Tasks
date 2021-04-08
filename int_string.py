  
def  change_index():
    mylist = [0,1,2]
    print("Pick a number from : ", mylist)

    result = False
    thenumbers = mylist
    while result == False:
        index_number= int(input("Choose a number from the list :"))
        if index_number in thenumbers:
            print("Cool now you can change the number with string you number is :", index_number)
            result = True
        else:
            print("Look at my list")
            result = False
 
        change_string = str(input("Enter a string or anything you want : "))
        
        mylist[index_number] = change_string
        print(mylist)
change_index()          