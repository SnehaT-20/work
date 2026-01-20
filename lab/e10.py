'''find which data type you cannot use in dictionary and find key rule to define

====> You can use:
        - int
        - float
        - string
====> you cannot use:
        - list
        - set
         
====> Key rules:
        -Keys must be unique
                d = {"a": 1, "a": 2}   # last value is stored
        
        - Keys must be immutable
        
        - Cannot change after creation
        
        - Keys cannot be list, set, or dictionary
        
        - Keys can be of different data types
                d = {1: "one", "2": "two"}
        
        - Values can be of any data type
                d = {"name": "Mona", "marks": [85, 90]}
'''