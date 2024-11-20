import random as r
import time
import os

o = ["🍇", "🍊", "🍌", "🍎", "🍈", "🍍", "🍏", "🍉", "🍋", "🥭", "🍐", "🍑", "🥝", "🍒", "🍅", "🍓", "🥑"]  # ,"🎰"
l = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]  # ,"🎰"

b = 200
pm = b
s = 0
x, y, z =0,0,0

# [-----------]
# [           ]
# [	         ]
# [	         ]
# [-----------]
def spin():
    global pm, b, s, x, y, z
    while True:
        if (b < 4.5):
            print("skrachoval si debilko, ale nevzdavaj sa predaj dom")
            print(f"prerobil si {pm} na {s} spinoch")
            break
        input()

        # x = l[r.randint(0, len(l) - 1)]
        # y = l[r.randint(0, len(l) - 1)]
        # z = l[r.randint(0, len(l) - 1)]
        vytocene = [r.choice(o) for i in range(3)]
        low = 0
        b -= 4.5
        s += 1
        while True:
            l = r.randint(0, len(o) - 1)
            for i in range(low, 3):
                try:
                    vytocene[i] = o[o.index(vytocene[i]) + 1]
                except:
                    vytocene[i] = o[0]
                if o[l] == vytocene[low]:
                    low += 1
            if low == 3:
                break
            os.system('cls')
            x, y, z = vytocene[0], vytocene[1], vytocene[2]
            print(f"[----------]\n[{x}][{y}][{z}]\n[----------]")
            # print(vytocene)
            time.sleep(0.05)
        # print(vytocene)
        # print(f"[{x}] [{y}] [{z}]")
        print(f"{o.index(x)} {o.index(y)} {o.index(z)}")
        if (o.index(x) == o.index(y) and o.index(y) == o.index(z)):

            print("jakopt ty kks")
            b += 700
            print(f"penaze: {b} + 700")
            # print("+700")
            pm += 700
        elif (o.index(x) == o.index(y) or o.index(y) == o.index(z)):
            b += 20
            print(f"penaze: {b} + 20")
            # print("+700")
            pm += 20
        else:
            print(f"penaze: {b} - 4.5")
            # print("-4,5")
        time.sleep(0.5)


predane = []


def shop():
    global b
    if (len(predane) < 5):
        print(f"mas {b} eurko")
        print(
            "1. predaj gauc za 55e \n2. predaj decko za 44e\n3. predaj manzelku za 200e(a ticho(konecne))\n4. predaj auto za 2000\n5. predaj barak za 10000")
        try:
            i = int(input("co predas?: "))
            if (i == 1):
                if (i in predane):
                    print("to si uz predal kamarat")
                else:
                    predane.append(i)
                    b += 55
                    print("predal si gauc\n+55e")
            elif (i == 2):
                if (i in predane):
                    print("to si uz predal kamarat")
                else:
                    predane.append(i)
                    b += 44
                    print("predal si decko\n+44e")
            elif (i == 3):
                if (i in predane):
                    print("to si uz predal kamarat")
                else:
                    predane.append(i)
                    b += 200
                    print("predal si manzelku\n+200e")
            elif (i == 4):
                if (i in predane):
                    print("to si uz predal kamarat")
                else:
                    predane.append(i)
                    b += 2000
                    print("predal si auto\n+2000e")
            elif (i == 5):
                if (i in predane):
                    print("to si uz predal kamarat")
                else:
                    predane.append(i)
                    b += 10000
                    print("predal si barak\n+10000e")
            elif (i > 5):
                print("taku vec nemas kamosko")
        except:
            print("zle ciselko kamosko")
        print("uz si secko predal ty zavislak")


while True:
    if (b < 4.5):
        shop()
    else:
        spin()
