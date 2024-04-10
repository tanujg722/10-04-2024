import random

def random_numbers(count):
    for _ in range(count):
        yield random.randint(1, 100)

# Using the generator
for num in random_numbers(5):
    print(num)
