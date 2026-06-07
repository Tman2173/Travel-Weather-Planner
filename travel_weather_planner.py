
distance_mi = float(input("How many miles do you have to travel today? "))
destination = input("What is your desination? ")


is_raining = input("Is it raining today? ")
if is_raining == "Yes" or is_raining == "yes":
    is_raining = True
else:
    is_raining = False

has_bike = input("Do you have a bicycle? ")
if has_bike == "Yes" or has_bike == "yes":
    has_bike = True
else:
    has_bike = False
    
has_car = input("Do you have a car? ")    
if has_car == "Yes" or has_car == "yes":
    has_car = True
else:
    has_car = False

has_ride_share_app = input("Could you use a ride share app? ")
if has_ride_share_app == "Yes" or has_ride_share_app == "yes":
    has_ride_share_app = True
else:
    has_ride_share_app = False


if distance_mi == False:
    print(f"{distance_mi} is a false value.")
elif distance_mi <= 1 and is_raining == False:
    print(f"You could walk to {destination}.")
elif (distance_mi > 1 and distance_mi <= 6) and has_bike and is_raining == False:
    print(f"Biking to {destination} would be good for you!")
elif distance_mi > 6 and (has_car or has_ride_share_app):
    print(f"Going to {destination} is a great idea!")
else:
    print(f"I wouldn't recommend traveling to {destination} due to the rain.")
