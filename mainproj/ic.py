import json
import os
import icecream as ic
import rich as r

path = r"C:\Users\margf\Downloads\f.txt"
with open(path, "r", encoding="utf-8") as f:
    complexjsn = json.load(f)
    ic.ic(complexjsn)
    r.print(r)
ic.ic("Fetching data")