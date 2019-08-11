prime_number = True
number = int(input("enter a number: "))

if number > 1:
    for i in range(2, number):
        reminder = number % i
        if reminder == 0:
            prime_number = False

    if prime_number:
        print(number, 'is a prime number')
    else:
        print(number, 'is not a prime number')
else:
    print("Enter any value greater than 1")
