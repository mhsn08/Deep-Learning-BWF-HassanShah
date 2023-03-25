try:
    with open("guest.txt","r") as f:
        print(f.read())
except:
    print("File Not Found")
finally:
    print("Done")



