#--- LOGICAL OPERATORS ---

#AND, OR, NOT


"""
Truth Table
-----------------------------
1. AND Logical Operator

5 < 10 and 5 > 2
5 < 20 and 5 > 0
20 < 10 and 10 > 5

Truth Table
[T][T] = [T]
[T][F] = [F]
[F][F] = [F]

2. OR Logical Operator

Truth Table
[T][T] = [T]
[T][F] = [T]
[F][F] = [F]

3. NOT Logical Operator

Truth Table
[T] = [F]
[F] = [T]

"""

#Storm signal categorizer

"""
Enter the wind speed
Determine the classification

< 80 [Droplets of rain]
80 - 100 [Signal #1]
100 - 150 [Signal #2]
150 - 200 [Signal #3]
"""

windSpeed = int(input("Enter wind speed: "))

if(windSpeed < 80):
    print("Droplets of rain")
elif(windSpeed >= 80 and windSpeed < 100):
    print("Signal #1")
elif(windSpeed >= 100 and windSpeed < 150):
    print("Signal #2")
elif(windSpeed >= 150 and windSpeed < 200):
    print("Signal #3")
else:
    print("Evacuate")