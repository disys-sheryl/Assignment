class contacts:
    data = int(input("Please enter initial number of contacts: ")), 5
     
   
    contacts = [{"name":1, "Mobileno":9884594997, "type":"personal", "favorite":"no"},
               {"name":"Aishwarya", "Mobileno":9884596875, "type":"personal", "favorite":"no"},
               {"name":"Ajit", "Mobileno":9785594997, "type":"personal","favorite":"no"},
               {"name":"Anand", "Mobileno":9885489997, "type":"personal", "favorite":"no"},
               {"name":"Angel", "Mobileno":9043551221, "type":"personal", "favorite":"no"},
               {"name":"Annie", "Mobileno":9884899051, "type":"personal", "favorite":"no"},
               {"name":"Ashwin", "Mobileno":9887395997, "type":"personal", "favorite":"no"},
               {"name":"Ayarin", "Mobileno":9882134997, "type":"personal", "favorite":"no"},
               {"name":"Ayesha", "Mobileno":9843874997, "type":"personal", "favorite":"no"},
               {"name":"Baby Nivetha", "Mobileno":9843874997, "type":"personal", "favorite":"no"},
               {"name":"Balaji Sir", "Mobileno":7904874997, "type":"office", "favorite":"no"},
               {"name":"Banu", "Mobileno":9043874997, "type":"personal", "favorite":"yes"},
               {"name":"Benedict", "Mobileno":9445874997, "type":"personal", "favorite":"no"},
               {"name":"Beni", "Mobileno":7904874152, "type":"personal", "favorite":"no"},
               {"name":"Benita", "Mobileno":9941874997, "type":"personal", "favorite":"no"},
               {"name":"Benny", "Mobileno":7904871221, "type":"personal", "favorite":"no"},
               {"name":"Betsy", "Mobileno":9941125152, "type":"personal", "favorite":"no"},
               {"name":"Blessy", "Mobileno":9941324282, "type":"personal", "favorite":"yes"},
               {"name":"Brindha", "Mobileno":9962096006, "type":"personal", "favorite":"no"},
               {"name":"Caesy", "Mobileno":9087202439, "type":"personal", "favorite":"yes"},
               {"name":"Caleb", "Mobileno":8600953421, "type":"personal", "favorite":"yes"},
               {"name":"Caroline", "Mobileno":9176495695, "type":"personal", "favorite":"yes"},
               {"name":"Christy", "Mobileno":7903874997, "type":"personal", "favorite":"no"},
               {"name":"Cibi", "Mobileno":8705432879, "type":"personal", "favorite":"no"},
               {"name":"Claston", "Mobileno":7904874668, "type":"personal", "favorite":"no"},
               {"name":"Dean", "Mobileno":9962096006, "type":"personal", "favorite":"no"},
               {"name":"Deepika", "Mobileno":9445662831, "type":"personal", "favorite":"no"},
               {"name":"Derrick", "Mobileno":9176495695, "type":"personal", "favorite":"yes"},
               {"name":"Divya Dharshini", "Mobileno":8609875439, "type":"personal", "favorite":"no"},
               {"name":"Dulip", "Mobileno":9884874997, "type":"personal", "favorite":"no"},
               {"name":"Dulip Jio", "Mobileno":7904874997, "type":"personal", "favorite":"no"},
               {"name":"Eddie", "Mobileno":8741937128, "type":"personal", "favorite":"no"},
                {"name":"Esther", "Mobileno":9043574997, "type":"personal", "favorite":"no"},
                {"name":"Fanny", "Mobileno":9445674997, "type":"personal", "favorite":"no"},
                {"name":"Ganesha", "Mobileno":9962074887, "type":"personal", "favorite":"no"},
                {"name":"Gawtham", "Mobileno":8743674677, "type":"personal", "favorite":"no"},
                {"name":"Gladson", "Mobileno":7904874437, "type":"personal", "favorite":"no"},
                {"name":"Gokul", "Mobileno":7904874439, "type":"personal", "favorite":"no"},
                {"name":"Hena", "Mobileno":7904878347, "type":"personal", "favorite":"no"},
                {"name":"Hephzibah", "Mobileno":8982846997, "type":"personal", "favorite":"no"},
                {"name":"Hepsi", "Mobileno":8823478897, "type":"personal", "favorite":"no"},
                {"name":"Home", "Mobileno":8934874997, "type":"personal", "favorite":"no"},
                {"name":"Ida", "Mobileno":9828747873, "type":"personal", "favorite":"no"},
                {"name":"Indu", "Mobileno":9827467437, "type":"personal", "favorite":"no"},
                {"name":"Ivin", "Mobileno":9218747377, "type":"personal", "favorite":"no"},
               {"name":"Jaanu", "Mobileno":6846546564, "type":"personal", "favorite":"no"},
               {"name":"Jaaziel", "Mobileno":9548563545, "type":"personal", "favorite":"no"},
               {"name":"Jacinth", "Mobileno":9265418655, "type":"personal", "favorite":"no"},
               {"name":"Jacob", "Mobileno":9518465636, "type":"personal", "favorite":"no"},
               {"name":"Jagan", "Mobileno":8618575316, "type":"personal", "favorite":"no"},
               {"name":"Jananiya", "Mobileno":7658465363, "type":"personal", "favorite":"no"},
               {"name":"Jasper", "Mobileno":8613847563, "type":"personal", "favorite":"no"},
               {"name":"Jaya", "Mobileno":9684684543, "type":"personal", "favorite":"no"},
               {"name":"Jeba", "Mobileno":7384684565, "type":"personal", "favorite":"no"},
               {"name":"Jeevitha", "Mobileno":7684646351, "type":"personal", "favorite":"no"},
               {"name":"Jena", "Mobileno":8574656566, "type":"personal", "favorite":"no"},
               {"name":"Jeni", "Mobileno":9216848455, "type":"personal", "favorite":"no"},
               {"name":"Jennifer", "Mobileno":7684688466, "type":"personal", "favorite":"no"},
               {"name":"Jessy", "Mobileno":8638546546, "type":"personal", "favorite":"no"},
               {"name":"Jeya Singh", "Mobileno":9658468454, "type":"personal", "favorite":"no"},
               {"name":"John", "Mobileno":9685768465, "type":"personal", "favorite":"no"},
               {"name":"Jona", "Mobileno":8687654655, "type":"personal", "favorite":"no"},
               {"name":"Julian", "Mobileno":9257878468, "type":"personal", "favorite":"no"},
               {"name":"Juliet", "Mobileno":7684635465, "type":"personal", "favorite":"no"},
               {"name":"Justin", "Mobileno":9285845665, "type":"personal", "favorite":"no"},
               {"name":"Kalai", "Mobileno":8464516354, "type":"personal", "favorite":"no"},
               {"name":"Kalaivani", "Mobileno":7648665165, "type":"personal", "favorite":"no"},
               {"name":"Kannan", "Mobileno":9618468453, "type":"personal", "favorite":"no"},
               {"name":"Karthik", "Mobileno":8485448646, "type":"personal", "favorite":"no"},
               {"name":"Kingston", "Mobileno":9384531531, "type":"personal", "favorite":"no"},
               {"name":"Kiruba", "Mobileno":9746565155, "type":"personal", "favorite":"no"},
               {"name":"Kishore", "Mobileno":9168475351, "type":"personal", "favorite":"no"},
               {"name":"Kowsalya", "Mobileno":9678435135, "type":"personal", "favorite":"no"},
               {"name":"Keerthana", "Mobileno":9678651635, "type":"personal", "favorite":"no"},
               {"name":"Lincy", "Mobileno":9353436136, "type":"personal", "favorite":"no"},
               {"name":"Linda", "Mobileno":8435416535, "type":"personal", "favorite":"no"},
               {"name":"Madhu", "Mobileno":8354683515, "type":"personal", "favorite":"no"},
               {"name":"Maha", "Mobileno":7684564561, "type":"personal", "favorite":"no"},
               {"name":"Manoj", "Mobileno":7905346515, "type":"personal", "favorite":"no"},
               {"name":"Merlin", "Mobileno":8456845341, "type":"personal", "favorite":"no"},
               {"name":"Michael", "Mobileno":8864651313, "type":"personal", "favorite":"no"},
               {"name":"Milne", "Mobileno":9686465135, "type":"personal", "favorite":"no"},
               {"name":"Monica", "Mobileno":9874765105, "type":"personal", "favorite":"no"},
               {"name":"Pavi", "Mobileno":9354684564, "type":"personal", "favorite":"no"},
               {"name":"Pavithra", "Mobileno":4564865846, "type":"personal", "favorite":"no"},
               {"name":"Pradeep", "Mobileno":9857574531, "type":"personal", "favorite":"no"},
               {"name":"Prem", "Mobileno":6847468455, "type":"personal", "favorite":"no"},
               {"name":"Presley", "Mobileno":4687148643, "type":"personal", "favorite":"no"},
               {"name":"Priya", "Mobileno":6878671845, "type":"personal", "favorite":"no"},
               {"name":"Puppy", "Mobileno":1837187175, "type":"personal", "favorite":"no"},
               {"name":"Rahul", "Mobileno":9861381384, "type":"personal", "favorite":"no"},
               {"name":"Raja", "Mobileno":9184715544, "type":"personal", "favorite":"no"},
               {"name":"Reji", "Mobileno":9185745575, "type":"personal", "favorite":"no"},
               {"name":"Reni", "Mobileno":8755135065, "type":"personal", "favorite":"no"},
               {"name":"Revathi", "Mobileno":8056451313, "type":"personal", "favorite":"no"},
               {"name":"Roseline", "Mobileno":9818545147, "type":"personal", "favorite":"no"},
               {"name":"Rubakumar", "Mobileno":8354650651, "type":"personal", "favorite":"no"},
               {"name":"Sam", "Mobileno":7681065105, "type":"personal", "favorite":"no"},
               {"name":"Sameera", "Mobileno":9684516541, "type":"personal", "favorite":"no"},
               {"name":"Sammy", "Mobileno":9614815161, "type":"personal", "favorite":"no"},
               {"name":"Sandhya", "Mobileno":9184196405, "type":"personal", "favorite":"no"},
               {"name":"Sandra", "Mobileno":9054161451, "type":"personal", "favorite":"no"},
               {"name":"Sanjay", "Mobileno":9158465451, "type":"personal", "favorite":"no"},
               {"name":"Sankar", "Mobileno":9034858065, "type":"personal", "favorite":"no"},
               {"name":"Sarah", "Mobileno":9158415051, "type":"personal", "favorite":"no"},
               {"name":"Saro", "Mobileno":8105064056, "type":"personal", "favorite":"no"},
               {"name":"Sathya", "Mobileno":8871016065, "type":"personal", "favorite":"no"},
               {"name":"Selvaraj", "Mobileno":9865030165, "type":"personal", "favorite":"no"},
               {"name":"Selvin", "Mobileno":9164515654, "type":"personal", "favorite":"no"},
               {"name":"Shakthi", "Mobileno":9158416484, "type":"personal", "favorite":"no"},
               {"name":"Shalini", "Mobileno":9761564165, "type":"personal", "favorite":"no"},
               {"name":"Shantha", "Mobileno":7180485551, "type":"personal", "favorite":"no"},
               {"name":"Sharmi", "Mobileno":8510456405, "type":"personal", "favorite":"no"},
               {"name":"Sharon", "Mobileno":8461085515, "type":"personal", "favorite":"no"},
               {"name":"Shiny", "Mobileno":7684604556, "type":"personal", "favorite":"no"},
               {"name":"Soniya", "Mobileno":9150651650, "type":"personal", "favorite":"no"},
               {"name":"Stephen", "Mobileno":9108040454, "type":"personal", "favorite":"no"},
               {"name":"Stephy", "Mobileno":7604051051, "type":"personal", "favorite":"no"},
               {"name":"Subhi", "Mobileno":9865065165, "type":"personal", "favorite":"no"},
              {"name":"Surya", "Mobileno":9865065165, "type":"personal", "favorite":"no"},
               {"name":"Swathi", "Mobileno":9865065165, "type":"personal", "favorite":"no"},
               {"name":"Tanisha", "Mobileno":9865065165, "type":"personal", "favorite":"no"},
               {"name":"Tharani", "Mobileno":9865065165, "type":"personal", "favorite":"no"},
               {"name":"Thossi", "Mobileno":9865065165, "type":"personal", "favorite":"no"},
               {"name":"Uma", "Mobileno":9865065165, "type":"personal", "favorite":"no"},
               {"name":"Vaisha", "Mobileno":9865065165, "type":"personal", "favorite":"no"},
               {"name":"Vaishu", "Mobileno":9865065165, "type":"personal", "favorite":"no"},
               {"name":"Varalakshmi", "Mobileno":9865065165, "type":"personal", "favorite":"no"},
               {"name":"Vasantha", "Mobileno":9865065165, "type":"personal", "favorite":"no"},
               {"name":"Vidhya", "Mobileno":9865065165, "type":"personal", "favorite":"no"},
               {"name":"Vignesh", "Mobileno":9865065165, "type":"personal", "favorite":"no"},
               {"name":"Viji", "Mobileno":9865065165, "type":"personal", "favorite":"no"},
               {"name":1, "Mobileno":9865065165, "type":"personal", "favorite":"no"}]

   # print(contacts)

    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit ")

    choice = int(input("Please enter your choice: "))
     

    
def __init__(self):
    
   
def add_contact():
    for i in contacts:
       
 
def remove_existing(contacts):
   
        input("Please enter the name of the contact you wish to remove: "))
    
  
            print(contacts.pop(i))
            
        if temp == 0:
       
        print("Sorry, you have entered an invalid query.\
    Please recheck and try again later.")
         
        return contacts
 
def delete_all(contacts):
   
    return contacts.clear()
 
def search_existing(contacts):
   
    choice = int(input("Enter search criteria\n\n\
    1. Name\n2. Number\n3. Email-id\n4. DOB\n5. Category(Family/Friends/Work/Others)\
    \nPlease enter: "))
    
 

def display_all(contacts):
    if not contacts:
   
        print("List is empty: []")
    else:
        for i in range(len(contacts)):
            print(contacts[i])
 
def thanks():

    print("Please visit again!")
    sys.exit("Goodbye, have a nice day ahead!")
 
# Main function 

print("Hello dear user, welcome to our smartphone directory system")
print("You may now proceed to explore this directory")

ch = 1
contacts = initial_phonebook()
while ch in (1, 2, 3, 4, 5):
    ch = menu()
    if ch == 1:
        pb = add_contact(contacts)
    elif ch == 2:
        pb = remove_existing(contacts)
    elif ch == 3:
        pb = delete_all(contacts)
    elif ch == 4:
        d = search_existing(contacts)
        if d == -1:
            print("The contact does not exist. Please try again")
    elif ch == 5:
        display_all(contacts)
    else:
        thanks()


