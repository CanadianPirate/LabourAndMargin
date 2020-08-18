# Simple program for adding margins

print("What margin would you like to add?")
while True:
	try:
		margin = float(input("Percent Number: "))
		margin = margin / 100
		margin = margin + 1
		break
	except (OSError, ValueError, TypeError):
		print("Please enter a number.")

while True:
	try:
		num = float(input("Price: "))
		num = num * margin
		num = round(num, 2)
		print("New Price: ", num)
	except (OSError, TypeError, ValueError):
		print("Please enter a number.")
