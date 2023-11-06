item_price=float(input("Input item price: "))
total_distance=float(input("Input total distance in km: "))
delivery= input("air or freight?").lower()
insurance=input("insurance- full or limited?").lower()
gift=input("gift- yes or no ").lower()
priority=input("priority- yes or no ").lower()
cost=0
if delivery=="air":
    cost=total_distance*0.36
elif delivery=="freight":
    cost=total_distance*0.25
else:
    print("Invalid delivery input, restart the program")
if insurance=="full":
    cost=cost+50
elif insurance=="limited":
    cost=cost+25
else:
    print("Invalid insurance input, restart the program")    
if gift=="yes":
    cost=cost+15
elif gift=="no":
    cost=cost+0
else:
    print("Invalid gift input, restart the program")    
if priority=="yes":
    cost=cost+100
elif priority=="no":
    cost=cost+20
else:
    print("Invalid priority input, restart the program")    
final_cost=cost+item_price   
print(final_cost)