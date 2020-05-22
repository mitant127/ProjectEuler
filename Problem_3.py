"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?"""

# from math import sqrt, ceil

NUMB = 600851475143
FACTOR = 2
PRIME_ARY = []
DIVIDER_ARY = []

while FACTOR <= NUMB:
    for i in PRIME_ARY:
        if FACTOR % i == 0:
            break
    else:
        PRIME_ARY.append(FACTOR)
        if NUMB % FACTOR == 0:
            DIVIDER_ARY.append(FACTOR)
            NUMB = NUMB / FACTOR
    FACTOR += 1

print(f"Max divider = {max(PRIME_ARY)}")
