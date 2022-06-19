def computepay(hrs, rph):
    if hrs <= 40:
        gp = hrs * rph
        return gp

    elif hrs > 40:
        hrsl = hrs - 40
        gp1 = (hrsl * (rph * 1.5))
        gp2 = 40 * rph
        gp = gp1 + gp2
     	return gp

# Prompt user for hours and rate per hour
hrs = float(input("Enter Hours: "))
rph = float(input("Enter rate per hour: "))

print("Pay " + str(computepay(hrs, rph)))
