data = [3, 8, 13, 18, 23]
weights = [2, 6, 13, 17, 12]
average = 16.1
a = 0
for i in range(len(data)):
    a += (data[i] - average) ** 4 * weights[i]
print(a)

b = sum(weights)
print(b)
print(a / 44670.605)
