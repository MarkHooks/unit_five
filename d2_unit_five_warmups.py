total_sum = 0

for x in range(1, 10001):
    if x % 3 == 0:
        total_sum = x + total_sum
print(total_sum)
# this will print 16668333
