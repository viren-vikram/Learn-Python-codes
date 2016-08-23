states = {
			'oregon':'or',
			'florida':'fl',
			'newyork':'ny',
			'california':'ca',
			'michigan':'mi'
}

cities = {
		'ca':'sanfransico',
		'mi':'detroit',
		'fl':'jacksonville'
		
		
		
			}

cities['ny'] = 'newyork'
cities['or'] = 'portland'


print('*'*10)
print("michigan abbreviation is  ",states['michigan'])
print("flordia has abbreviation", states['florida'])

print("*"*10)

print("michigan has following cities : ", cities[states['michigan']])
print("florida has ",cities[states['florida']])

print("-"*10)


for abbrev, city in cities.items():
	print("%s has following %s city" %(abbrev,city))
	
print("***"*10)
	
for state, abbrev in states.items():
	print("%s has abbrev %s & has cities %s" %(state,abbrev,cities[abbrev] ))
	
print("*"*10)

state = states.get("texas")

if not state:
	print("soory texas not in the list")

city = cities.get('tx', 'does not exist')
print("the city n texas state is % s" %city)