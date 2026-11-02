# Write a program that reads the number N and then any numbers until the user
# enters N different numbers.
# After reading, the program prints all the different numbers entered, as well as, sepa-
# rately, those entered more than once.

def main():
    n = int(input("Enter a number N: "))

    unique_numbers = []
    repeated_numbers = []

    while len(unique_numbers) < n:
        temp = int(input("Enter any number: "))
        if temp not in unique_numbers:
            unique_numbers.append(temp)
        else:
            if temp not in repeated_numbers:
                repeated_numbers.append(temp)

    print("Different numbers:", unique_numbers)
    print("Repeated numbers:", repeated_numbers if repeated_numbers else ["None"])
if __name__ == "__main__":
    main()
