def main():
    while 1:
        count = 1
        base = input("Enter a base: ")
        try:
            power = input("Enter a power: ")
            if int(power) < 0:
                raise IndexError
        except:
            print("Use a non-negative exponent please")
        number = base
        recursive(int(base), int(number), int(power), int(count))


def recursive(base, number, power, count):
    if count < power:
        number = base * number
        count += 1
        recursive(base, number, power, count)
    else:
        print(f"Answer: {number}")
        main()


main()