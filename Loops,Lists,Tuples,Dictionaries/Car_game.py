print("Enter help to see commands")
h=input()
print("start-to start the car")
print("stop-to stop the car")
print("quit-to exit")

ip=input()
started=False
while ip.lower()!=quit:
    
    if ip=="start":
        if started:
            print("Car already started")
        else:
         started=True
         print("Car started....Ready to go!")
    elif ip=="stop":
        if not started:
            print("Car already stopped")
        else:
         started=False
         print("Car stopped")
    elif ip=="quit":
        print("End")
        break
    else:
        print("I dont understand that...")
    ip=input()

   
