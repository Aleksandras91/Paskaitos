import time

# Number of iterations
N = 100_000_000  

# FOR LOOP
start = time.time()
total_sum_for = 0
for i in range(N):
    total_sum_for += i
end = time.time()
print(f"For loop time: {end - start:.4f} s, sum={total_sum_for}")

# WHILE LOOP
start = time.time()
total_sum_while = 0
count = 0
while count < N:
    total_sum_while += count
    count += 1
end = time.time()
print(f"While loop time: {end - start:.4f} s, sum={total_sum_while}")
 