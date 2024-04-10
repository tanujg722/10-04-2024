def squares_up_to(limit):
    n = 1
    while n <= limit:
        yield n ** 2
        n += 1

# Using the generator
for square in squares_up_to(5):
   print(square)





