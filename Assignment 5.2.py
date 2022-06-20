nums = []
largest = None
smallest = None
running = True
while running:
    try:
        num = input("Enter a number: ")
        nums.append(int(num))
    except:
        if num == "done":
        	running = False
           	break
        print("Invalid input")

largest = max(nums)
smallest = min(nums)

print("Maximum is", largest)
print("Minimum is", smallest)
