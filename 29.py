import cmath

# Read input and convert to complex number
z = complex(input().strip())

# Modulus
r = abs(z)

# Phase angle
phi = cmath.phase(z)

# Print results
print(r)
print(phi)