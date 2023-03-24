import time

start = time.time()

l1 = ["eat", "sleep", "repeat"]

obj1 = enumerate(l1)

print ("Return type:", type(obj1))
print (list(enumerate(l1)))

end = time.time()

print(f"Runtime of the program is {end - start}")

