#main function to ask user what mode and value they want
#and passes info to recursive functions
def main():
    while 1:
        mode = input("Enter mode:")
        value = input("Enter a value: ")
        value = int(value)
        if mode == "-i":
            if value == 1:
                print("0")
            elif value == 2:
                print("1")
            else:
                number = 0
                one_before = 1
                count = 2
                recursive_i(int(value), int(count), int(number), int(one_before))
        elif mode == "-v":
            if value == 1:
                print("1 is in the sequence")
            elif value == 2:
                print("2 is in the sequence")
            else:
                number = 0
                one_before = 1
                recursive_v(int(value), int(number), int(one_before))

#i method recursion that finds the fibonacci number of
#any value in fibonacci sequence as inputed by user
def recursive_i(value, count, number, one_before):
    store = number
    number = one_before + number
    one_before = store
    if count == value:
        print(f"Fibonacci: {number}")
        main()
    else:
        count += 1
        recursive_i(value, count, number, one_before)

#v method recursion that checks if value is in fibonacci sequence
def recursive_v(value, number, one_before):
    store = number
    number = number + one_before
    one_before = store
    if number == value:
        print(f"{value} is in the sequence")
        main()
    elif number > value:
        print(f"{value} is not in the sequence")
    else:
        recursive_v(value, number, one_before)

main()