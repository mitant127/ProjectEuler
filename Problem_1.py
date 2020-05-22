"""If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of
all the multiples of 3 or 5 below 1000."""

N = 0
N2 = 1000
SUM_N = 0

while N < N2:
    if N % 3 == 0 or N % 5 == 0:
        SUM_N += N
        # print(SUM_N, N)
    N += 1
print(f"Summ = {SUM_N}")
