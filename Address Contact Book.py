friendslist = open("Friendslist.txt","r")
friendslistnew = open("Friendslistnew.txt", "w")

friends = list()

while True:
    friend_search = input ("Do you want to view, add, erase or update contacts? Type \"end\" to finish the program.\n")
    contact_found = False
    if friend_search.lower()!= "view" and friend_search.lower()!="add" and friend_search.lower()!="erase" and friend_search.lower()!="update" and friend_search.lower()!="end":
        print("Invalid Input.\n")
    elif friend_search.lower() == "end":
        break
    else:
        for friend in friendslist:
            friends.append(friend)
        if friend_search.lower() == "view":
            friends.sort()
            for line in friends:
                print (line.rstrip())
        elif friend_search.lower() == "add":
            contact_name = input ("Enter contact Name: ")
            contact_position = input ("Enter contact Position: ")
            contact_number = input ("Enter contact Phone Number: ")
            contact_email = input ("Enter contact Email ")
            contact_info = contact_name + " - " + contact_position + ", " + contact_number + ", " + contact_email + "\n"
            friends.append(contact_info)
        elif friend_search.lower() == "erase":
            contact_name = input("Enter contact Name: ")
            for line in friends:
                if line.startswith(contact_name)==True:
                    friends.remove(line)
                    contact_found=True
            if contact_found == False:
                print ("contact is not found in the database.\n")
        elif friend_search.lower() == "update":
            contact_name = input("Enter contact Name: ")
            for line in friends:
                if line.startswith(contact_name)==True:
                    contact_found = True
                    while True:
                        contact_info_select = input ("Which info do you want to change? Position, number or email?\n")
                        if contact_info_select.lower() == "position" or contact_info_select.lower() == "number" or contact_info_select.lower() == "email":
                            break
                    contact_info = line.split("-")
                    contact_update = contact_info[1]
                    contact_update_new = contact_update.split(",")
                    contact_position = contact_update_new[0].strip()
                    contact_number = contact_update_new[1].strip()
                    contact_email = contact_update_new[2].strip()
                    if contact_info_select.lower() == "position":
                        contact_position = input ("Please type in new position: ".strip())
                    elif contact_info_select.lower() == "number":
                        contact_number = input("Please type in new phone number: ".strip())
                    elif contact_info_select.lower() == "email":
                        contact_email = input("Please type in new email: ".strip())
                    friends.remove(line)
                    contact_info = contact_name + " - " + contact_position + ", " + contact_number + ", " + contact_email + "\n"
                    friends.append(contact_info)
                    break
            if contact_found==False:
                print ("contact is not found in the database")

friends.sort()
for line in friends:
    friendslistnew.write(line)


friendslist.close()
friendslistnew.close()
