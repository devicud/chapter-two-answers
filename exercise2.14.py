user_age = int(input("Enter your age: "))
max_heartrate = 220 - user_age
target_heartrate1 = 50/100 * max_heartrate
target_heartrate2 = 85/100 * max_heartrate
print (f"Your maximum Heart-Rate is {max_heartrate}\nYour average Heart-Rate is within the range of {target_heartrate1} and {target_heartrate2}")