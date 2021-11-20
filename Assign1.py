# JORDAN BUCKINDALE [251246279]

# The program will compute and display the cost of electricity (including discounts and tax).
# The program will prompt the user for the information of power usage.

# Determine constants and set variables

OFF_PEAK_RATE = float(0.085)
ON_PEAK_RATE = float(0.176)
MID_PEAK_RATE = float(0.119)
TAXRATE = float(1.13)                    # Amount total cost plus tax

TOTAL_USAGE_LIMIT = 400.0
ON_PEAK_MINIMUM = 150.0

# Set discounts
totalUsageLimitDiscount = float(.96)    # amount cost after discount
onPeakDiscount = float(.95)
seniorDiscount = float(.89)



# Set prompt for input data.
while True:
        offPeakPeriod = float(input("Enter kwh during Off Peak period: "))
        if offPeakPeriod == 0:
            break
        onPeakPeriod = float(input("Enter kwh during On Peak period: "))
        midPeakPeriod = float(input("Enter kwh during Mid Peak period: "))




# Determine if residence belongs to senior
        senior = input("Is the owner a senior?(Y,y,N,n): ")


# Set variable for total kwh used
        totalKilowatts = offPeakPeriod + onPeakPeriod + midPeakPeriod

# Get subtotals of each peak period
        offPeakPeriodCost = offPeakPeriod * OFF_PEAK_RATE
        onPeakPeriodCost = onPeakPeriod * ON_PEAK_RATE
        midPeakPeriodCost = midPeakPeriod * MID_PEAK_RATE

# Set subtotal of peak periods without discount
        peakTotalCost = offPeakPeriodCost + onPeakPeriodCost + midPeakPeriodCost

# Set up specifications for discount
        if totalKilowatts < TOTAL_USAGE_LIMIT:
            totalUsageSavings = peakTotalCost - (peakTotalCost * totalUsageLimitDiscount)
        else:
            totalUsageSavings = 0

        if (0 < onPeakPeriod < ON_PEAK_MINIMUM) and totalUsageSavings == 0:
            onPeakSavings = onPeakPeriodCost - (onPeakPeriodCost * onPeakDiscount)
        else:
            onPeakSavings = 0

# Set up variable
        seniorSavings = 0
        seniorTotal = peakTotalCost - (totalUsageSavings + onPeakSavings)

# Calculate Senior Discount
        if senior == "y":
            seniorSavings = seniorTotal - (seniorTotal * seniorDiscount)
        if senior == "Y":
            seniorSavings = seniorTotal - (seniorTotal * seniorDiscount)

# Set up variables
        totalSavings = totalUsageSavings + onPeakSavings + seniorSavings

# Calculate total cost
        totalCost = (peakTotalCost - totalSavings) * TAXRATE

# Display electricity cost
        print("Electricity cost: $%.2f" % totalCost)
