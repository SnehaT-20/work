lst_city=["dwarka","rajkot","ahemdabad","ab","mehsana","mumbai"]
count=0
for i in lst_city:
    if i.startswith('m'):
        print(i)
        count+=1
print(f"no of string{count}")