def my_sqrt(n, tolerance=0.0001):
    approx = n/2
    closer = (approx + n/approx)/2
    while abs(closer - approx) > tolerance:
        approx = closer
        closer = (approx + n/approx)/2
    return closer

n = float(input("Enter a positive floating point number: "))
while n <= 0:
    print("Invalid input. Please enter a positive floating point number.")
    n = float(input("Enter a positive floating point number: "))
print("Approximate square root of number:", my_sqrt(n))