'''

ID|name|DOB|Gender|Age|Zip code|Amount

1000|John Smith |01/01/2000|F|20|08122-2324|1500.20

2000|Jim McDonald |02/02/2020|M|25|08136-2324|1500.20

20|Jim McDonald|02/02/1999|M|25|08124-6565|1500.20

'''



data = {"customer": {"1000": {"ID": "1000", "name": "John Smith ", "DOB": "01/01/2000",
                            "Gender": "F", "Age": "20","Zip code": "08122-2324", "Amount ": "1500.20"},
                   "2000": {"ID": "2000", "name": "Jim McDonald ", "DOB": "02/02/2020",
                            "Gender": "M", "Age": "25","Zip code": "08136-2324","Amount ": "1500.20"},
                   "20": {"ID": "20", "name": "Jim McDonald", "DOB": "02/02/1999",
                          "Gender": "M", "Age": "25","Zip code": "08124-6565","Amount ": "1500.20"}}}
        
for i in data.values():
    for j in i.values():
        for k,l in j.items():
            if(k=="name"):
                temp=l
            if(k=="Age" and int(l)<25):
                print(temp,k,l)

