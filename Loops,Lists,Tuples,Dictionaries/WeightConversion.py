wt=int(input("Enter your Weight"))
s=input("Enter what unit u have entered weight in, K for kg or L for lbs")
j="k"
if s.lower()==j:
    print(f"Weight in lbs:{(wt/0.45)}")
else:
    print(f"Weight in kg:{(wt*0.45)}")