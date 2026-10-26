# Write a program defining two lists of ints, e.g.:
# numbs = [256, 81, 256, 82, 27, 16807, 456]
# divis = [ 16, 3, 8, 9, 3, 7, 4]
# For consecutive pairs of numbers, say n and d, where n is from numbs and d is from
# divis, the program prints whether n is a power of d.

def main():
    numbs = [256, 81, 256, 82, 27, 16807, 456]
    divis = [ 16, 3, 8, 9, 3, 7, 4]

    for i in range(len(numbs)):
        n = numbs[i]
        d = divis[i]
        temp = n
        while temp > 1 and temp % d == 0:
            temp = temp / d
        if temp == 1:
            print(f"{n} is a power of {d}")
        else:
            print(f"{n} is not a power of {d}")

    return 0

if __name__ == "__main__":
    main()
