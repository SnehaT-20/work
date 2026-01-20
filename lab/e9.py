''' Create a list of tuples where each tuple contains:
student name & marks
	Then print the name of the student who scored the highest marks.'''
students = [("Mona", 85),("Mohnish", 92),("Nitin", 88),("Sneha", 95)]
min("mona")
print(min(students))



''' Tuple Comparison
Create two tuples and check:
which one is larger
if they are equal'''
tup1=(11,20,11)
tup2=(20,11,11)
if tup1>tup2:
    print("tup1 is greater")
elif tup1<tup2:
    print("tup2 is greater")
else:
    print("Both tuples are equal")


''' Reverse a List (Without reverse())'''
lst_city=["dwarka","rajkot","ahemdabad","ab"]
for i in range(len(lst_city)-1,-1,-1):
    print(lst_city[i])
