def cheese_and_crackers(cheese_count, box_of_crackers):
	print("you have %d cheese" %cheese_count)
	print("you have %d cracker boxes" %box_of_crackers)
	print("just get a blanket \n")
	
print("we can just give this function numbers directly")
cheese_and_crackers(20,30)

print("or we can give value to the variables ")

amount_cheese = 10
amount_crackers = 50

cheese_and_crackers(amount_cheese,amount_crackers)


print("wecan do the math inside these functions as well")
cheese_and_crackers(10+20,20+50)

print("can combine variable and math too")
cheese_and_crackers(amount_cheese+10,amount_crackers +20 )

