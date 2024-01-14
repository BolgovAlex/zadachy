f = open('26-1.txt')
amount, budget = map(int, f.readline().split())
ans1 = 0
bars = []
for _ in range(amount):
    taste, price, quantity = f.readline().split()
    bars += [[taste, int(price), int(quantity)]]
f.close()
bars.sort(key=lambda x: (x[1]))
for i in range(amount):
    if budget - bars[i][1] * bars[i][2] < 0:
        break
    if bars[i][0] == 'O' and budget > 0:
        budget -= bars[i][1] * bars[i][2]
for i in range(amount):
    if budget - bars[i][1] * bars[i][2] < 0:
        break
    if bars[i][0] == 'F':
        ans1 += bars[i][2]
        budget -= bars[i][1] * bars[i][2]
for i in range(amount):
    if budget - bars[i][1] * bars[i][2] < 0:
        break
    if bars[i][0] == 'K':
        budget -= bars[i][1] * bars[i][2]
while budget - bars[i][1] > 0:
    budget -= bars[i][1]
print(ans1, budget)
