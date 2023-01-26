import math

a = int(input("Enter Value of side A: "))
b = int(input("Enter Value of side B: "))
c = int(input("Enter Value of side C: "))
if a+b > c and b+c > a and c+a > b:
    s = (a+b+c)/2
    print("The area of Triangle is: " ,math.sqrt(s*(s-a)*(s-b)*(s-c)))
else:
    print("The Triangle is Invalid.")