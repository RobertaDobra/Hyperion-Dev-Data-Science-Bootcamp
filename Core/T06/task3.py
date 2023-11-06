swimming_time=float(input("Input time taken for swimming in minutes:"))
cycling_time=float(input("Input time taken for cycling in minutes:"))
running_time=float(input("Input time taken for running in minutes:"))
qualifying_time=100
total_time=swimming_time+cycling_time+running_time
if total_time <= qualifying_time:
    print("Provincial Colours")
elif total_time >qualifying_time and total_time <= qualifying_time+5:
    print("Provincial Half Colours")
elif total_time >qualifying_time and total_time <= qualifying_time +10:
    print("Provincial Scroll")
elif total_time > qualifying_time +10:
    print("No award")