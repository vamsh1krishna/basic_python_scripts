f =input("Enter temperature in Fahrenheit: ")
try:
    ff = float(f)
except :
    print("Enter a numerical value")
    quit()
x = (ff-32)*5/9
print(x,"C")
