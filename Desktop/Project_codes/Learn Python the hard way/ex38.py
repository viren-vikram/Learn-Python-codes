ten_things = "Apples oranges crows telephone light sugar"

print("wait there are not ten things in this list, lets make it right")

stuff = ten_things.split(' ')

more_stuff =["day", "night","summer", "winter","lets", "go","in", "alto" ]

while len(stuff)<10:
	next_one = more_stuff.pop()
	print("adding ",next_one)
	stuff.append(next_one)
	print("there are %d items now" %len(stuff))
	
print("there we go ",stuff)
print("lets do something with this")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
