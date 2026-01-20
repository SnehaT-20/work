lst1=[1,2,3,4]
lst2=[1,2,9,16]
ans=list(zip(lst1,lst2))
print(ans)


data=[('gujarat','rajkot')]
lst_state,lst_city=zip(*data)
print(lst_state)
print(lst_city)

'''write a program to find a sqaure of a number and stor it into another list'''

lst2=[1,22,6]
ans=[]
#for i in lst2 # 
 #   ans.append(i*i)
 #   print(i)

ans=[i*i for i in lst2 if i%2==0]
print(ans)

#convert lst element into upper case with list comprehensive
lst_country=['usa','india']
answer=[i.upper() for i in lst_country]
print(answer)