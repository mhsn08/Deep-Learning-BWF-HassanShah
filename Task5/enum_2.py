import time

start = time.time()


l1 = ["eat", "sleep", "repeat"]

for i in enumerate(l1):
    print (i)

end = time.time()

print(f"Runtime of the program is {end - start}")


