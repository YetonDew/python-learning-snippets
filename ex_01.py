# Write a program that reads three integers from the user, a, b, and c. The user enters
# these numbers in binary, octal, and hexadecimal, respectively. Treating these num-
# bers as coefficients of a quadratic equation, the program calculates the discriminant
# (“delta”) and, depending on its value, displays a message informing about the number
# of real roots.

def main():
    a = input("Please enter a number in binary base: ")
    b = input("Please enter a number in octal base: ")
    c = input("Please enter a number in hexadecimal base: ")

    a = int(a, 2)
    print(f"a = {a}")
    b = int(b, 8)
    print(f"b = {b}")
    c = int(c, 16)
    print(f"c = {c}")

    print(f"Δ = {b}^2 - 4 * {a} * {c}")
    delta = b**2 - 4 * a * c
    print(f"Δ = {delta}")

    if (delta > 0):
        print(f"for the values {a}, {b} and {c} has two real solutions.")
    elif (delta == 0):
        print(f"for the values {a}, {b} and {c} has one real solutions.")
    else:
        print(f"for the values {a}, {b} and {c} has no real solutions.")

if __name__ == "__main__":
    main()
