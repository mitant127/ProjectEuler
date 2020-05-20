# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

n = 600851475143
n2 = 1
i = 2

print(n)
while True:

    if n % i == 0:

        if n2 < i:
            n2 = i
            n = n / i
            i = 1

            if n == 1:
                break

    i += 1

print(f"Max divider = {n2}")
