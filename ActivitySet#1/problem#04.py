hours = float(input("Enter Hours:"))
rate=float(input("enter the rate:"))
p1 = hours *rate
p2=  (hours-40)*(rate*1.5)+40*rate

if (hours<=40):
    print(p1)
else:
  print(p2)