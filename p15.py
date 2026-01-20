''' 	
Print list of items iteratively among with type of data e.g lst_collection = ['A',True,234,45.76] output = A - chr
                                                                                                   True - bool
                                                                                                   234 - int
                                                                                                   45.76 - float
'''
lst_city=['Dwarka','Rajkot','ahmedabad',20,11,20.11]
for i in lst_city:
    print(f"{i} = {type(i).__name__}")
    