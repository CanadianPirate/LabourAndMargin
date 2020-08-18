# Modified version of the Labour estimator with utmost speed in mind on the user end


# Function to calculate total labour cost
def lab_total():
    try:
        total_cost = hour_cost * hour_amount
        print("Total Cost: $" + str(total_cost))
    except (OSError, ValueError, TypeError):
        pass


while True:
    try:
        hour_amount = float(input("Please enter the cost per hour: "))
        hour_cost = float(input("Please enter the total hours worked: "))
        lab_total()
    except (TypeError, ValueError):
        print("Please enter only numbers")
