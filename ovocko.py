import random as r
import time

l = ["🍇", "🍊", "🍌", "🍎", "🍈", "🍋", "🍍","🍏","🍉","🍋‍","🥭","🍐","🍑","🥝","🍒","🍅","🍓","🥑"] #,"🎰"

b = 450
pm = b
while True:
	if(b<=4.5):
		print("skrachoval si kokotko, ale nevzdavaj sa predaj dom")
		print(f"prejebal si {pm}")
		break
	#input()

	x = l[r.randint(0, len(l)-1)]
	y = l[r.randint(0, len(l)-1)]
	z = l[r.randint(0, len(l)-1)]
	b-=4.5
	print(f"penaze: {b}")
	print(f"[{x}] [{y}] [{z}]")
	if(x == y and y == z):
		print("jakopt ty kks")
		b+= 700
		print("+700")
		pm+=700
	else:
		print("-4,5")
	time.sleep(0.01)
		