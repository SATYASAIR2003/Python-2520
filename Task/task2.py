# Bill with Discharge
Amount=int(input("Enter your amount: "))
if Amount<2000:
    print("No Disount")
elif Amount<3000:
    Dis=20
    print(f"You get 20% off")
elif Amount<4000:
    Dis=30
    print("You get 30% off ")
else:
    Dis=40
    print("You get 40% off ")
Total = Amount-(Amount*Dis/100)
print(f"your final money is {Total}")
