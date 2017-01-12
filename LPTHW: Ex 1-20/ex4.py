#assigning the variable cars
cars = 100
#assigning the variable space_in_a_car as floating point
space_in_a_car = 4.0
#assigning the variable drivers
drivers = 30
#assigning the variable passengers
passengers = 90
#Caluclating the no of people doesn't drive a car and storing in cars_not_driven
cars_not_driven = cars - drivers
#Caluclating the no of people who drive a car and storing in cars_driven
cars_driven = drivers
#Caluclating the no of paople the car can fit and storing in carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
#Caluclating the average no of passengers as average_passengers_per_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
