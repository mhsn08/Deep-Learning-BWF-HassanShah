try:
    with open("guest.txt","a") as f:
        print("Enter Guests Name, Press 0 to exit")
        while(1):
            name = input("Name: ")
            if(name == '0'):
                break
            f.write(name)
            f.write("\n")
except:
    print("Failed to Open the file")
finally:
    print("Done")




