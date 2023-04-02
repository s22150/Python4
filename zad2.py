def prime(*number_list):

    for number in number_list:
        if number == 2:
            print(f"{number} is prime")
        elif number == 1 or number == 0 or number % 2 == 0:
            print(f"{number} is not prime")
        else:
            sqrt = number ** 0.5
            is_prime = True
            for i in range(3, int(sqrt) + 1, 2):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(f"{number} is prime")
            else:
                print(f"{number} is not prime")


prime(0, 1, 2, 3, 4, 5)
