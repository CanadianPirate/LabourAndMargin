# Modified version of the Labour estimator with utmost speed in mind on the user end

# Setting variable
hour_cost = 95


# Function to calculate total labour cost
def lab_total():
    try:
        total_cost = hour_cost * hour_amount
        print("Total Cost: $" + str(total_cost))
    except (OSError, ValueError, TypeError):
        pass


while True:
    try:
        hour_amount = float(input("Please enter a number: "))
        lab_total()
    except (TypeError, ValueError):
        print("Please enter only numbers")