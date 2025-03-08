a = int(input())
b = int(input())
c = int(input())
d = a * b * c
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while d > 0:
    i = d % 10
    count[i] += 1
    d //= 10

for i in range(10):
    print(count[i])
