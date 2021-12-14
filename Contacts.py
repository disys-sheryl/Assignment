contacts_details = {"Dean":9176495695,"Jessy":9087202439}

print(contacts_details)

   
class contacts:
    def __init__(self):
        self.number=int(input("Enter No.of.contacts:"))

        for i in range(self.number):
            self.name=input("Enter Contact Name :")
            self.mobileno=int(input("Enter Mobile Number:"))
            key=self.name
            value=self.mobileno
            contacts_details[key]=value
        main()

    def displaycontact(self):
        print(contacts_details)
        
       
   
def add_contact():
    name=input("Enter Name:")
    mobileno=input("Enter Number:")
    if(len(mobileno)>10):
        raise ValueError("Number invalid")
    else:
        contacts_details[name]=mobileno
    main()


    
def remove():
    name=input("Enter the Name:")
    contacts_details.pop(name)
    main()

    
 
def delete_all(contacts_details):
   
    return contacts_details.clear()

    main()
 
def display_all(contacts_details):

    if not contacts_details:
        print("List is empty: []")
    else:
        print(contacts)
        
def quit():
    print("Exit")
    
 
# Main function

def main():

    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Display all contacts")
    print("5. Exit ")
    ch=int(input("Enter your choice:"))

    if(ch==1):
        add_contact()
    elif(ch==2):
        remove()
    elif(ch==3):
        delete_all(contacts_details)
    elif(ch==4):
        display_all(contacts_details)
    else:
        exit()



fb=contacts()
fb.displaycontact()
main()
    

   




