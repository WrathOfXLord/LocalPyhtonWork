import sys
n = []
i = input().split(",")


for x in range(len(i)):
    n.append(float(i[x]))
n.sort()

answer = 0.0
if len(n) % 2 == 0:
    answer = (n[int((len(n) - 1) / 2)] + n[int(len(n) / 2)]) / 2
else:
    print(int(len(n) / 2))
    answer = n[int(len(n) / 2)]
# for i in range(x):
#     n[i] = int(x[i])
print(answer)

