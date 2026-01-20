dict1={"India":"gujarat", "UAE":"dubai","France":"Paris","england":"London"}
print(dict1)
print(dict1["India"])
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print("keys:===================")
for i in dict1.keys():
    print(i)
for i in dict1.keys():
    print(dict1[i])

print("values:===============  ")
for i in dict1.values():
    print(i)

print("keys and values:==================   ")
for i, j in dict1.items():
    print(i,j)

''' get give none as output if key is not there '''
dict1 = {"sneha":789089,"Romil":56789,"Vishwraj":9090}
print(f"Before update {dict1}")
dict1.update({"dharmshtha":3434})
print(f"After update {dict1}")

# dict1.clear()
# print(f"After clear {dict1}")

new_dict=dict1.copy()
print("NEW DICTIONARY",new_dict)

lst1=["Abhijit","Mahesh"]
dict2=dict1.fromkeys(lst1)
print("After fromkeys ",dict1)
print("After fromkeys ",dict2)
dict3=dict1.fromkeys(dict1.keys())
print("After fromkeys ",dict3)

print(dict1.get("567657"))
#print(dict1["567657"])

print(f"pop method {dict1.pop("sneha")}")
print(f"After pop dict {dict1}")

print(dict1.popitem())
print(f"After popitem dict {dict1}")

dict1.setdefault("Mahesh",234234)

dict1["Mahesh"]=9999
print(f"After setdefault dict {dict1}")
