# Write a program that reads the number N and then any numbers until the user
# enters N different numbers.
# After reading, the program prints all the different numbers entered, as well as, sepa-
# rately, those entered more than once.

def main():
    n = int(input("Enter a number N: "))
    isUnique = True
    isRepeated = True

    unique_numbers = []
    repeated_numbers = []

    while len(unique_numbers) < n:
        temp = int(input("Enter any number: "))
        for unique in unique_numbers:
            if unique == temp:
                isUnique = False
        if isUnique:
            unique_numbers.append(temp)
        else:
            for repeated in repeated_numbers:
                if repeated == temp:
                    isRepeated = False
            if isRepeated:
                repeated_numbers.append(temp)
        isUnique = True
        isRepeated = True
    print("Different numbers:", unique_numbers)
    print("Repeated numbers:", repeated_numbers if repeated_numbers else ["None"])
if __name__ == "__main__":
    main()
