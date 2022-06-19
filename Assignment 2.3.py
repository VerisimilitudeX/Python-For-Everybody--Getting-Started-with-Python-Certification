# Prompt user for hours and rate per hour
hrs = input("Enter Hours:")
rph = input("Enter Rate Per Hour: ")

# Calculate gross pay
gp = float(hrs) * float(rph)

# Print result
print("Pay: " + str(gp))
