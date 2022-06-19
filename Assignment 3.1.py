# Prompt user for hours and rate per hour
hrs = float(input("Enter Hours:"))
rph = float(input("Enter rate per hour: "))

# Calculate gross pay
if hrs <= 40:
	gp = hrs * rph
    
elif hrs > 40:
    hrsl = hrs - 40
    gp1 = (hrsl * (rph * 1.5))
    gp2 = 40 * rph
    gp = gp1 + gp2

# Print result
print(str(gp))
