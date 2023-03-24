dict1 = {1:['Jon','Doe','Paris'],
         2:['Lionel','Messi','Argentina'],
         3:['Eden','Hazard','Belgium']}

for key in dict1:
    print(f"{key}: {dict1[key]}")
    

dict1[4] = ["Osmane","Dembele","France"]
for key in dict1:
    print(f"{key}: {dict1[key]}")
    

del(dict1[1])
for key in dict1:
    print(f"{key}: {dict1[key]}")
    

dict1[4] = ["Osmane","Dembele","Barcelona"]
for key in dict1:
    print(f"{key}: {dict1[key]}")
    

