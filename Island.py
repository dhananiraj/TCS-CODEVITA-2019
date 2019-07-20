n1 = int(input())
st = []
cou1 = 0
while cou1 != n1:
    st1 = input()
    st = st + [st1]
    cou1 = cou1 + 1

war = input()

final_arr = []

cou2 = 0
while cou2 != n1:
    li = st[cou2].split(" ")

    final = [li[0] + " " + li[1]] + [li[2] + " " + li[3]] + [li[0] + " " + li[3]] + [li[2] + " " + li[1]]

    f = war.split(" ")
    cou = 0
    stor = []
    count = 0
    while count != 4:
        v = final[cou]
        str1 = v.split(" ")
        val = abs(int(f[0]) - int(str1[0])) + abs(int(f[1]) - int(str1[1]))
        stor = stor + [val]

        count = count + 1

    final_arr.append((cou2, min(stor)))
    cou2 = cou2 + 1


def sortingfun(y):
    return y[1]


final_arr.sort(key=sortingfun)

for i in final_arr:
    print(i[0] + 1)

# 3
# 1 1 0 0
# 1 2 2 3
# 3 0 4 1
# 0 4
