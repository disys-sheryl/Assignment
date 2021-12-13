Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> swiggy=[{"a2b":[{"area":"adayar","rating":"4.0","most rated":"vegitarian"},{"area":"perambur","rating":"3.9","most rated":"sweets"} ],
 "anjappar":[{"area":"ashoknagar","rating":"4.2","most rated":"non veg"},{"area":"tambaram","rating":"4.1","most rated":"fried rice"}],
 "thalapakatti":[{"area":"tiruvottiyur","rating":"4.5","most rated":"briyani"},{"area":"tiruvanmiyur","rating":"4.6","most rated":"bucket briyani"}],
 "ss hyderabad":[{"area":"kolathur","rating":"4.3","most rated":"briyani"},{"area":"manali","rating":"4.7","most rated":"bucket briyani"}],
 "pushpa":[{"area":"koyambedu","rating":"3.8","most rated":"masalapoori"},{"area":"velacherry","rating":"4.9","most rated":"parotta"}],
 "locofeast":[{"area":"nungambakkam","rating":"4.1","most rated":"grillchcken"},{"area":"madipakkam","rating":"4.2","most rated":"chillychicken"}],
 "bbq":[{"area":"tnagar","rating":"4.9","most rated":"unlimited buffet"},{"area":"porur","rating":"4.3","most rated":"smokebiscuit"}],
 "haunted":[{"area":"annanagar tower","rating":"4.9","most rated":"potato nuggets"},{"area":"annanagar east","rating":"3.9","most rated":"theme"}],
 "kfc":[{"area":"mambalam","rating":"3.5","most rated":"chicken popcorn"},{"area":"mandaveli","rating":"3.6","most rated":"chickrn lollipop"}],
 "yamohideen":[{"area":"velacherry","rating":"4.5","most rated":" beefbriyani"},{"area":"guindy","rating":"4.8","most rated":"fried rice"}],
 "bismillah":[{"area":"kathipara","rating":"4.3","most rated":"dumbriyani"},{"area":"madipakkam","rating":"4.7","most rated":"chickenbriyani"}],
 "althaf":[{"area":"velacherry","rating":"4.7","most rated":"pepperchicken"},{"area":"saidapet","rating":"4.8","most rated":"schezwan"}],
 "pizzahut":[{"area":"royapuram","rating":"4.9","most rated":"cheese pizza"},{"area":"tondiarpet","rating":"4.5","most rated":"burger"}],
 "rideus":[{"area":"adampakkam","rating":"4.5","most rated":"chicken65"},{"area":"kaiveli","rating":"4.8","most rated":"pakoda"}],
 "rasavid":[{"area":"kalmandapam","rating":"4.5","most rated":"non veg"},{"area":"kaladipet","rating":"4.3","most rated":"dessert"}],
 "oyalo":[{"area":"tolgate","rating":"3.5","most rated":"butter pizza"},{"area":"teradi","rating":"4.5","most rated":"chicken pizza"}],
 "pandiyas":[{"area":"tiruvottiyur","rating":"4.5","most rated":"briyani"},{"area":"tiruvottiyur","rating":"4.5","most rated":"briyani"}],
 "chettinad":[{"area":"talambur","rating":"3.8","most rated":"meals"},{"area":"navallur","rating":"3.9","most rated":"lunch"}],
 "alif":[{"area":"mount","rating":"4.4","most rated":"briyani"},{"area":"littlemount","rating":"4.5","most rated":"rice"}],
 "waterffalls":[{"area":"vadapalani","rating":"4.5","most rated":"combo"},{"area":"ekkatuthangal","rating":"4.5","most rated":"theme"}],
 "thoppivapa":[{"area":"taramani","rating":"4.5","most rated":"chilliparotta"},{"area":"perungudi","rating":"4.5","most rated":"chilliparotta"}],
 "ecrfastfood":[{"area":"triplicane","rating":"4.5","most rated":"chickenrice"},{"area":"lighthous","rating":"4.5","most rated":"chillychicken"}]}]

for i in swiggy:
    if (i["a2b"][0]["area"]=="adayar"):
        print("order food")
    if (i["anjappar"][1]["rating"]=="4.2"):
        print("order food")
    if (i["thalapakatti"][0]["area"]=="tiruvottiyur"):
        print("order food")
    if (i["haunted"][1]["rating"]=="4.9"):
        print("book table")
    if (i["althaf"][0]["area"]=="velacherry"):
        print("order rice")
    if (i["oyalo"][0]["area"]=="tolgate"):
        print("order pizza")
    if (i["chettinad"][1]["rating"]=="3.8"):
        print("book slot")


for i  in swiggy:
    for j in i.values():
        for k in j:
            print(k)
