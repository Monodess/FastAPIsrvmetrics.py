#from [name] import [...] unlocks namespace
#import [name] as [...] keeps namespace
import json
import os

#formatted prints for db
import icecream as ic
import rich as r


login = os.getlogin()
if login == "Professional":
    path = r"C:\Users\Professional\Documents\Elder Scrolls Online\live\AddOnSettings.txt"
else:
    path = r"C:\Users\margf\Downloads\f.txt"

if os.path.exists(path):
    ic.ic("hi")
    try:
        with open(path, "r", encoding="utf-8") as f:

               complex_json = f.read()
            print(f"something went wrong")
            print(complex_json)
            # for simple "print"
            ic.ic(complex_json)

            # for complex obj
            r.print(r)
            
    except Exception as e:
        complex_json = f.read()
        print(f"something went wrong")
        print (complex_json)
else:
    ic.ic("File doent exist")

ic.ic("Fetching data")
