# Normal human body temperature in 98.6 °F. Convert it to Celsius. (F = 1.8 * C + 32)
f = 98.6
c = (f - 32) / 1.8
print(f"Normal human body temperature in Celsius: {c:.2f} °C")

# Calculate simple interest for Rs. 50,000 at rate 6.5% p.a for 4 years. (SI = PTR/100)
P = 50000
R = 6.5
T = 4
SI = (P * T * R) / 100
print(f"Simple Interest: Rs. {SI:.2f}")

# Calculate area & perimeter of circle with diameter 12 cm. (Area = πr², P = 2πr)
import math
d = 12
r = d / 2
area = math.pi * r ** 2
perimeter = 2 * math.pi * r
print(f"Area of circle: {area:.2f} cm²")
print(f"Perimeter of circle: {perimeter:.2f} cm")

# Calculate the total seconds in 3 hours, 20 minutes and 45 seconds.
hours = 3
minutes = 20
seconds = 45
total_seconds = (hours * 3600) + (minutes * 60) + seconds
print(f"Total seconds: {total_seconds} seconds")

# Calculate the average of 5 subjects where marks are: 78, 85, 62, 90 and 88.
marks = [78, 85, 62, 90, 88]
average = sum(marks) / len(marks)
print(f"Average marks: {average:.2f}")

# Convert the distance of 15 kilometers to miles. (1 km = 0.621371 miles)
km = 15
miles = km * 0.621371
print(f"Distance in miles: {miles:.2f} miles")

# Calculate the BMI for a person with weight 70 kg and height 1.75 m. (BMI = wt / ht²)
weight = 70
height = 1.75
bmi = weight / (height ** 2)
print(f"BMI: {bmi:.2f}")
# Calculate the compound interest for amount Rs. 50,000 at rate 6.5% p.a compounded annually for 4 years. (CI = P(1 + r/n)^(nt) - P)
P = 50000
R = 6.5 / 100
T = 4
n = 1  # compounded annually
CI = P * (1 + R / n) ** (n * T) - P
print(f"Compound Interest: Rs. {CI:.2f}")
print(type(CI))
