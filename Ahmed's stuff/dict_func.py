names = {"ahmed" : "29th" , "hamza" : "30th"}
names.setdefault("ali" , "31st")
print(dict.keys(names))
print(dict.items(names))
for i in names.keys():
    print(i)
for k in names.items():
    print(k)
import pprint
print(pprint.pprint(names))






