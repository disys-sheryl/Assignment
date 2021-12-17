fb_friends = {"Dean":"Dean.W","Jessy":"Jessy.Jean","Sammy":"Sam.W","Caesy":"Caesy.A","Caroline":"Caroline.A"}

grp_friends = ["Dean","Jessy","Sam"]
#print(fb_friends)  
class facebook:
    def __init__(self):
        self.number=int(input("Enter No.of.friends:"))

        for i in range(self.number):
            self.name=input("Enter Friend Name :")
            self.fbid=input("Enter friend's Facebook ID:")
            key=self.name
            value=self.fbid
            fb_friends[key]=value
        main()

    def display(self):
        print(fb_friends)
        
       
   
def add_friends():
    name=input("Enter Name:")
    fbid=input("Enter FbID:")
    fb_friends[name]=fbid
    main()


    
def unfriend():
    name=input("Enter the Name:")
    fb_friends.pop(name)
    main()


def groups():
    for i in grp_friends :
        if i in fb_friends.values():  
            print(i)

def quit():
    print("Exit")


def main():

    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Group Friends")
    print("4. Exit ")

    ch=int(input("Enter your choice:"))

    if(ch==1):
        add_friends()
    elif(ch==2):
        unfriend()
    elif(ch==3):
        groups()
    else:
        exit()



obj=facebook()
#obj.group()
#obj.display()
main()
