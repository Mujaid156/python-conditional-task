speed_limit = int(input("Enter speed limit km/h:"))
speed = int(input("Enter your speed in km/h:"))
points = (speed - speed_limit)/5

if speed <=60:
    print("OK")
elif speed > speed_limit:
    if points < 12:
        print("Demerit points:" + str(points))
    elif points > 12:
        print("You are going to jail. Demerit points:" + str(points))
