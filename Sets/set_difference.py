from primes_and_squares import squares_generator, primes_generator

evens = set(range(0, 50, 2))
odds = set(range(1, 50, 2))

print("evens: ", evens)
print("odds:", odds)

primes = set(primes_generator(100))
print("primes:", primes)

squares = set(squares_generator(100))
print("squares", squares)

#difference method returns a new set which exist only in the first set and not in the second
#thus order of appearance is important. In this case if we want the unique items from odds
#set which are not present in primes. We write it in this way:
print(odds.difference(primes))
#minus operator does the same jobs
print(odds - primes )
