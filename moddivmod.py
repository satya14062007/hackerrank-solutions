from __future__ import division

def main():
    # Read input integers
    a = int(input().strip())
    b = int(input().strip())

    # Calculate and print results
    print(a // b)  # Integer division
    print(a % b)   # Modulo operator
    print(divmod(a, b))  # divmod function

if __name__ == "__main__":
    main()
