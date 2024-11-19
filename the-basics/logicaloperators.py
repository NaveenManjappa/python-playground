# logical operators = evaluate multiple conditions ( or , and, not)
# or = at least one condition must be True
# and = both conditions must be True
# not = inverts the condition

temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("Outdoor event is cancelled")
else:
    print("The outdoor event is scheduled")

temp2 = 20
is_sunny = False

if temp2 >= 28 and is_sunny:
    print("It's HOT outside 🥵")
    print("It is Sunny ☀️")
elif temp2 <= 0 and is_sunny:
    print("It is COLD outside ❄️")
    print("It is SUNNY")
elif 28 > temp2 > 0 and is_sunny:
    print("It is WARM outside ")
    print("It is SUNNY")
elif temp2 >= 28 and not is_sunny:
    print("It's HOT outside 🥵")
    print("It is CLOUDY ☁️")
elif temp2 <= 0 and not is_sunny:
    print("It is COLD outside ❄️")
    print("It is CLOUDY ☁️")
elif 28 > temp2 > 0 and not is_sunny:
    print("It is WARM outside ")
    print("It is CLOUDY ☁️")