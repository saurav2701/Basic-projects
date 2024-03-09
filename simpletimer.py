import time 


def timer(t): 
    while t:  

        #returns minute and sec of given sec
        mins , sec = divmod(t , 60)  

        timer = "{:02d} : {:02d}".format(mins , sec)  

        print(timer , end ="\r")  

        time.sleep(1) 

        t -= 1  

    print("Timer complete") 


t = input("Tnter time in seconds : ") 

timer(int(t)) 

