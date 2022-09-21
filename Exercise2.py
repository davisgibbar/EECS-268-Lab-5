def main():
    while 1:
        try:
            day = input("Enter number of days flu has existed: ")
            day = int(day)
            if day <= 0:
                raise RuntimeError
        except:
            print("Invalid day")
        if day == 1:
            print("Total people with flu: 6")
        if day == 2:
            print("Total people with flu: 20")
        if day == 3:
            print("Total people with flu: 75")
        if day >= 4:
            number = 75
            one_before = 20
            two_before = 6
            count = 4
            recursive(day, int(count), int(number), int(one_before), int(two_before))


def recursive(day, count, number, one_before, two_before):
    store = number
    number = number + one_before + two_before
    two_before = one_before
    one_before = store
    if count == day:
        print(f"Total people with flu: {number}")
        main()
    else:
        count += 1
        recursive(day, count, number, one_before, two_before)

main()