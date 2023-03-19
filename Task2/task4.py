print("Changing,Adding,Removing")

l = ["Saad","Rehan","Farhan"]
print(l[1],"Can't make it")
l[1] = "Jawad"

for i in l:
    print("Invite",i)

l.insert(0,"Ahmad")
l.insert(1,"Ammar")
l.append("Amir")

while(len(l)>2):
    print("Sorry",l.pop())

del(l[0])
del(l[0])
print(l)

print("___________________________")
print("Organizing")

locations = ["Madina","Mecca","Barcelona","Calafornia","Doha"]
for i in locations:
    print(i)

locations.sort()
for i in locations:
    print(i)

print("reverse")
for i in range(len(locations)-1,-1,-1):
    print(locations[i])

print("Orignal Again")
for i in locations:
    print(i)



locations.reverse()
print("reverse function")
for i in locations:
    print(i)

locations.sort()
print("sorted")
for i in locations:
    print(i)

locations.sort(reverse=True)
for i in locations:
    print(i)


print(len(l))
print("All Guests were deleted;)")


