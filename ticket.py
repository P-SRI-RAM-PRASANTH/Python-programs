class Ticket:
    def caughtSpeeding(speed,birthday):
        if(speed<=65 and birthday or speed<=60):
            print(0)
        elif(speed<=85 and birthday or speed<=80):
            print(1)
        else:
            print(2)
obj=Ticket

obj.caughtSpeeding(60, False)  
obj.caughtSpeeding(65, False) 
obj.caughtSpeeding(65, True) 
obj.caughtSpeeding(80, False) 
obj.caughtSpeeding(85, False)  
obj.caughtSpeeding(85, True) 
obj.caughtSpeeding(70, False) 
obj.caughtSpeeding(75, False)  
obj.caughtSpeeding(75, True) 
obj.caughtSpeeding(40, False)
obj.caughtSpeeding(40, True)  
obj.caughtSpeeding(90, False) 

