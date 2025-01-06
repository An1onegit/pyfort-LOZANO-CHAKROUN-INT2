import random

def math_challenge():
    x = random.randint(1, 4)
    match x:
        case 1:
            return math_challenge_factorial()
        case 2:
            return math_challenge_prime()
        case 3:
            return math_roulette_challenge()
        case 4:
            return math_challenge_equation()

def math_challenge_factorial():
    n = random.randint(1,10)
    print(f"Math Challenge: Calculate the factorial of {n}")
    answer = 1
    for i in range(1,n+1) :
        answer *= i
    guess = int(input(f"Your answer: "))
    if guess == answer :
        print("Correct! You win a key.")
        return True
    else :
        print("Wrong ! Loser...")
        return False

def math_challenge_equation():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print(f"Math Challenge : Solve the equation {a}x+{b} = 0")
    x = float(input("What is the value of x : "))
    if solve_linear_equation(a,b,x):
        print("Correct! The key is yours.")
        return True
    else:
        print("Wrong ! Get good.")
        return False

def solve_linear_equation(a, b, x):
    if a*x + b == 0:
        return True
    else :
        return False

def math_challenge_prime():
    number = random.randint(10,20)
    print(f"Math Challenge: Find the nearest prime to {number}.")
    x = int(input("Your answer: "))
    if is_prime(x):
        if nearest_prime(number) == x:
            print("Correct! The key is yours.")
            return True
        else:
            print("Wrong !")
            return False
    else:
        print("Wrong !")
        return False

def is_prime(n):
    divisor = 0
    b = 1
    while b <= n:
        if n % b == 0:
            divisor += 1
        b += 1
    if divisor > 2 or n == 1:
        return False
    else:
        return True

def nearest_prime(n):
    x = n
    while not is_prime(x):
        x += 1
    return x

def math_roulette_challenge():
    numbers = []
    for i in range(5):
        numbers.append(random.randint(1,20))
    print("Numbers on the roulette: ", numbers)
    operation = random.randint(1,3)
    result = numbers[0]
    match operation:
        case 1:
            print("Calculate the result by combining these numbers with addition")
            for i in range(1, len(numbers)):
                result += numbers[i]
            x = int(input("Your answer: "))
            if x == result:
                print("Correct answer! You've won a key.")
                return True
            else:
                print("Incorrect answer!")
                return False
        case 2:
            print("Calculate the result by combining these numbers with subtraction")
            for i in range(1, len(numbers)):
                result -= numbers[i]
            x = int(input("Your answer: "))
            if x == result:
                print("Correct answer! You've won a key.")
                return True
            else:
                print("Incorrect answer!")
                return False
        case 3:
            print("Calculate the result by combining these numbers with multiplication")
            for i in range(1, len(numbers)):
                result *= numbers[i]
            x = int(input("Your answer: "))
            if x == result:
                print("Correct answer! You've won a key.")
                return True
            else:
                print("Incorrect answer!")
                return False
