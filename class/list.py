'''lst_name = ['sneha','mona']
print(lst_name)
for i in lst_name:
    print(i)'''

'''lst_num = [1,2,3,4,5]
sum=0
for i in lst_num:
    if type(i)==int or type(i)==float:
        sum+=i
print(f"total of element is{sum}")'''

lst_city=["dwarka","rajkot","ahemdabad","ab"]
'''for i in lst_city:
    for j in i:
        if j in "AEIOUaeiou":
            print(i)
            break
   # print(f"{i}={len(i)}")'''
''' convert to upper case if the len of string is more than 5'''
for i in lst_city:
    if len(i) >=5:
        print(i.upper())
    else:
        print(i)
# access element through index
for i in range(len(lst_city)):
    print(lst_city[i])

'''lab work := check the list contains valid mobile number or not'''
''' append = word ma word j lye but new list krva maq e aakhi list ne j ek element banavi nakhe che
    extend= word ma cgaracter ne element lye che'''


       
   
lst_city=["dwarka","rajkot","ahemdabad","ab"]
for i in range(len(lst_city)-1,-1,-1):
    print(lst_city[i])