import math
print("investment- to calculate the amount of interest you will earn on your investment")
print("bond- to calculate the amount you will have to pay on a home loan ")
x=str(input("Enter either 'investment' or 'bond' from the menu above to proceed: ")).lower()
if x=="investment":
    P=float(input("Enter amount of money you are depositing:"))
    r=float(input("Enter the number of the interest rate, without the percentage sign (%): "))/100
    t=int(input("Enter number of years you plan on investing: "))
    interest=str(input("Enter 'simple' or 'compound': "))
    if interest=="simple":
        A = P * ( 1 + r * t )
        print("Total amount= " + str(A))
    elif interest=="compound":
        A = P * math.pow( ( 1 + r ) , t )
        print("Total amount= " + str(A))
elif x=="bond":
    P=float(input("Enter present value of the house: "))
    i=float(input("Enter the number of the monthly interest rate, without the percentage sign (%): "))/(12*100)
    n=int(input("Enter number of years you plan to take in order to repay the bond: "))
    A=(i*P)/(1-(1+i)**(-n))
    print("Repayment=" + str(A))
else:
    print("Please enter a valid input. Try again.")  