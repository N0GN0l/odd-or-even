numbers = int(input("How many numbers would you like to detect up to?: "))
print('num = input("What is ur number?: ")')
for i in range(numbers + 1):
    print("if num == " + str(i) + ":")
    if (i % 2) == 0 :
        print('\tprint("Your number is even")')
    else:
        print('\tprint("Your number is odd")')