#PiApproximation.py

"""This program will take an error tolerance from the user and find the minimum
number of terms required to get an approximation of Pi."""

row = 1

error_tol = float(input("Input error tolerance:"))

print()

print("Number of Terms \t Pi Approximation")

PI = 3.14159265358979
pi_app = 0
k = 1
calcerror_tol = PI
while calcerror_tol >= error_tol:
    pi_app = pi_app + (4*(-1)**(k+1))/(2*k-1)
    print(row, "\t", "\t", "\t", "\t", "\t", pi_app)
    k += 1
    row += 1
    calcerror_tol =abs(PI - pi_app)

print()
k -= 1

print(f"After {k} terms, pi is approximately  {pi_app:.6f}.")    
print(f"Our error is {calcerror_tol:.6f} which is less than or equal to {error_tol}.")
