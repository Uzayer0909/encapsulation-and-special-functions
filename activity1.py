class myclass:


    #private variable 
    __privateVar = 50


    #private method 
    def __privateMethod(self):
        print("I am a private method. I cannot be accesed from outside strangers.")


    def printVar(self):
            print(myclass.__privateVar)




ob = myclass()
ob.printVar()
ob.__privateMethod()
