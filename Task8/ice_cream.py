class resturant:
    def __init__(self,name,cuisine):
        self.name = name
        self.cuisine = cuisine
    
    def desc_rest(self):
        print(f"Resturant Name: {self.name}\nCuisine Type: {self.cuisine}")
        
    def open_rest():
        print("The Resturant is open")
        

class ice_cream(resturant):
    def __init__(self,name,cuisine,flavours):
        super().__init__(name,cuisine)
        self.flavours = flavours
    
    def desc_rest(self):
        super().desc_rest()
        print("Flavours:")
        for i in range(len(self.flavours)):
            print(f"{i}:{self.flavours[i]}")
        
l = []
        
    
while(1):
    print("Press 1 to add ice-cream resturant")
    print("Press 2 to view information")
    print("Press 3 to check if its open")
    i = int(input("Press: "))
    if(i == 1):
        name = input("Resturant Name: ")
        cuisine = input("Cuisine: ")
        l2 = []
        while(1):
            print("Press 0 to stop adding")
            flavour = input("Add Flavour: ")
            l2.append(flavour)
        l.append(ice_cream(name,cuisine,flavour))
    elif(i == 2):
        name = input("Resturant Name: ")
        for j in l:
            if(j.name == name):
                j.desc_rest()
                break
    elif(i == 3):
        name = input("Resturant Name: ")
        for j in l:
            if(j.name == name):
                j.open_rest()
                break
    else:
        break
        
        
        
