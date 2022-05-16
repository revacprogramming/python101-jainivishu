def computepay(hrs, rte):
 pay = (hrs-40)*rte*1.5+ 40*rte
 return pay
    
     
def main():
 hrs = float(input("Enter hours?"))
 rte = float(input("Enter rate per hour"))
 pay= computepay(hrs,rte)
 print("Pay",pay)

main()