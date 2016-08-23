Cars = 100
Space_in_a_car = 4.0
Drivers = 30
Passengers = 90
Cars_not_Driven = Cars - Drivers
Cars_driven = Drivers
Carpool_capacity = Cars_driven * Space_in_a_car
Average_passenger_per_car = Passengers / Cars_driven

print ( "There are", Cars, "cars available")
print ( "there are only", Drivers, "drivers available")
print ( "There will be ", Cars_not_Driven, "empty cars today")
print ( "we can transport" , Carpool_capacity, "people today" )
print ( "we have", Passengers, "to carpool today")
print ("we need to put about ", Average_passenger_per_car, "in each car today ")
