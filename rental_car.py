import sys

'''
Section 1: Collect customer input
'''

##Collect Customer Data - Part 1

##Request Rental code to start:


rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")

#Request time period the car was rented.

#Prompt --> "Number of Days Rented:"
#rentalPeriod = input("Number of Days Rented:\n")
#	OR
#Prompt --> "Number of Weeks Rented:"

if rentalCode == "B" or rentalCode == "D":
  rentalPeriod = int(input("Number of Days Rented:\n"))
else:
  rentalPeriod = int(input("Number of Weeks Rented:\n"))


#Pricing variables:
budgetCharge = 40.00
dailyCharge = 60.00
weeklyCharge = 190.00

#Calculation Part 1
#For this Calculation Part 1: need to set price variables
if rentalCode == "B":
  baseCharge = rentalPeriod * budgetCharge
if rentalCode == "D":
  baseCharge = rentalPeriod * dailyCharge
if rentalCode == "W":
  baseCharge = rentalPeriod * weeklyCharge

#in order to get the decimal placeds we need the '.2f' format
print(format(baseCharge, '.2f'))

#Prompt the user to input the starting odometer reading and store it as the variable odoStart
#Variables for odometer are as follow:
#Prompt -->"Starting Odometer Reading:\n"
# odoStart = ?

OdoStart = float(input("Starting Odometer Reading:\n"))

#Prompt the user to input the ending odometer reading and store it as the variable odoEnd

#Prompt -->"Ending Odometer Reading:"
# odoEnd = ?
OdoEnd = float(input("Ending Odometer Reading:\n"))

##c) Calculate total miles
totalMiles = OdoEnd - OdoStart



# Calculate Charges for miles driven


mileCharge = (totalMiles * .025)

## To cacluate miles per day and add it to the calculations
#--this if statement needed to be created 

averageDayMiles = totalMiles/rentalPeriod
if averageDayMiles <= 100:
  extraMiles = 0
else:
  extraMiles = averageDayMiles - 100
  mileCharge = extraMiles * 0.25
#print(mileCharge)

## In order to calculate mileCharge for the rentalPeriod
#--weekly I needed to creat anothe rif statement
averageWeekMiles = totalMiles/rentalPeriod
if averageWeekMiles >= 900:
  mileCharge = rentalPeriod * 100
else:
  mileCharge = 0.00
#print(mileCharge)

#create a variable for amount due
amtDue = baseCharge + mileCharge

print("Rental Summary")
print("Rental Code" + ":" + " " + rentalCode)
print("Rental Period" + ":" + " " + str(rentalPeriod))
print("Starting Odomenter" + ":" + " " + str(OdoStart))
print("Ending Odometer" + ":" + " " + str(OdoEnd))
print("Miles Driven" + ":" + " " + str(totalMiles))
print("Amount Due" + ":" + " " + "$" + str('%.2f' % amtDue))
