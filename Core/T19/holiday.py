def hotel_cost(nights): #is a function of nights stayed at the hotel
    return 45*nights 
    
def plane_cost(city): #is a function of city you are flying to
    if city=="London":
        return 70
    elif city=="Paris":
        return 80
    elif city=="Rome":
        return 60
    elif city=="New York":
        return 100
    else:
        return 0 #one answer is possible because of if, elif, else

def car_rental(days): #is a function of days the car is rented for
    return 15*days

def holiday_cost(nights, city, days):
    nights = hotel_cost(nights) #hotel_cost function defined above is applied to nights
    city = plane_cost(city) #function applied
    days = car_rental(days) #function applied
    return nights + city + days #after 3 functions applied, add the values resulting

nights = int(input('How many nights will you be staying? '))
city = str(input('Where are you flying to? '))
days = int(input('How many days will you rent a car: ')) #arguments are inputted 
total = holiday_cost(nights, city, days) #function is called
print("Your total cost is: " + str(total))