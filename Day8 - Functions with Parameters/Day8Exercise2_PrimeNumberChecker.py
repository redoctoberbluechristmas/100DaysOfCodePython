def prime_checker(number):

    if number > 1:
        for i in range(2, number):
            if number % i == 0: 
                print("It's not a prime number.")
                #Don't forget break, or you'll get multiple resposnes when you only want one.
                break
        else:
            print("It's a prime number.")

    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)