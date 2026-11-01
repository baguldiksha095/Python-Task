print("welcome to the interactive Personal Data Collector!")
a=input("Please enter your name: ")
b=int(input("Please enter your age: "))
c=float(input("Please enter your height in meters: "))
d=int(input("Please enter your favorite number: "))

print("Thank you! Here is the information we collected:")

print("Name:", a,("Type:", type(a), "id:", id(a)))
print("Age:", b,("Type:", type(b), "id:", id(b)))
print("Height:", c,("Type:", type(c), "id:", id(c)))
print("Favorite Number:", d,("Type:", type(d), "id:", id(d)))
h=2026-int(b)

print("Your Birth year is approximately:",h,"(based on your age of",b,")")

print("Thank you for using the Personal Data Collector.Goodbye!")
