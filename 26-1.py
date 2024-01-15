f = open('26-1.txt')
amount, budget = map(int, f.readline().split())
ans1 = 0
j=0
bars = []
for _ in range(amount):
    taste, price, quantity = f.readline().split()
    bars += [[taste, int(price), int(quantity)]]
f.close()
bars.sort(key=lambda x: (x[1]))
for i in range(amount):
    if bars[i][0] == 'O':
        if budget - bars[i][1] * bars[i][2] < 0:
            j=i
            break
        budget -= bars[i][1] * bars[i][2]
for i in range(amount):
    if bars[i][0] == 'F':
        if budget - bars[i][1] * bars[i][2] < 0:
            j=i
            break
        ans1 += bars[i][2]
        budget -= bars[i][1] * bars[i][2]
for i in range(amount):
    if bars[i][0] == 'K':
        if budget - bars[i][1] * bars[i][2] < 0:
            j=i
            break
        budget -= bars[i][1] * bars[i][2]
while budget - bars[j][1] > 0:
    if bars[j][2] > 0:
        budget -= bars[j][1]
        bars[j][2] -= 1
    if bars[j][2] <= 0:
        j+=1
print(ans1, budget)
