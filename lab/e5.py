'''
startswith		-	LabTask
replace			-	LabTask
find			-	 LabTask
trim			-		LabTask
rtrim			-		LabTask
ltrim			-		LabTaskprint'''

name=input("enter your name  ")
print(f"{name.find("t")}")
print(f"{name.replace("T","t")}")
print(f"{name.startswith("t")}")
print(f"trim {name.lstrip()}")
print(f"trim {name.rstrip()}")
print(f"trim {name.strip()}")