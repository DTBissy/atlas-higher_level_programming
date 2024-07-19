import random
number = random.randint(-500, 500)
if number < 0:
    print(f"{number} The number is negative")
elif number == 0:
    print(f"{number} The number is zero")
elif number > 0:
    print(f"{number} The number is positive")
elif number % 10:
    print(f"{number} is a funky number")