'''check the list co,ntains valid mobile numbers or not
lst = ['test1234','1234567890','9090909090',4567890,9876543211,'45654','3345testwe']
isdigit ,isalphanumeric 
output :1234567890
		9090909090
		9876543211'''

lst = ['test1234', '1234567890', '9090909090', 4567890, 9876543211, '45654', '3345testwe']
for i in lst:
    s = str(i)           # convert to string
    if s.isdigit() and len(s) == 10:
         print(i)