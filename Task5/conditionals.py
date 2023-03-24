l = ['admin','Eric','Jon','Doe','Adam']
for i in l:
    if i == 'admin':
        print('Hello admin,would you like to see a status report?')
    else:
        print('Hello',i)

def if_emp(l):
    if len(l) == 0:
        print("We need to find somw users")
    else:
        print("We do have some users")


current_users = ['admin','Eric','Jon','Doe','Adam']
new_users = ['Eric','Magnus','Jon','Wick','Karl']
check_l = []
for i in current_users:
    check_l.append(i.lower())
for i in new_users:
    if(i.lower() not in check_l):
        print(i,"is available")
    else:
        print(i,"is not not available")
        


