def computepay(hrs, rte):
  if hrs>40:
   pay = (hrs-40)*rte*1.5+ 40*rte
  else:
   pay=hrs*rte
  return pay

def main():
    hrs=float(input("Enter hours?"))
    rte=float(input("Enter rate per hour"))
    p = computepay(hrs,rte)
    print("Pay",p)

main()