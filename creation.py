numbers = int(input("How many numbers would you like to detect up to?: "))
with open('effective_detector.txt', 'w') as effective:
    effective.write('num = input("What is ur number?: ")\n')    
    for i in range(numbers + 1):
        effective.write("if num == " + str(i) + ":\n" )
        if (i % 2) == 0 :
            effective.write('\tprint("Your number is even")\n')
        else:
            effective.write('\tprint("Your number is odd")\n')
    effective.write('\f if num > {numbers}: \n print("go away bruh")')
    