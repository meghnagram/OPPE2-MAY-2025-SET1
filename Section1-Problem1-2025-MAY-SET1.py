def compute_electricity_bill(units: int) -> float:
    """
    Calculate the electricity bill.

    - <=200 units : 0.5 per unit
    - <= 400 units : 0.75 per unit + 150 extra
    - > 400 units : 0.90 per unit + 300 extra

    Args:
        units (int): Number of units consumed.

    Returns:
        float: Total amount to be paid.
    """
    
    
    if units <= 200:
        cost = units * 0.5
    elif units <= 400:
        cost = units * 0.75 + 150
    else:
        cost = units * 0.90 + 300
    
    return cost

# #Another Method:

# def compute_electricity_bill(units: int) -> float:
    
#     if units<=200:
#         return units*0.5
#     elif units <=400:
#         return units*0.75 + 150
#     else:
#         return units*.90+300
    
#     #return cost

# Compute Electricity Bill
# Write a function compute_electricity_bill that returns the electricity bill amount based on the number of units consumed.

# If the units consumed are less than or equal to 200, the cost per unit is 0.5.
# If the units consumed are less than or equal to 400, the cost per unit is 0.75 plus a fixed extra charge of Rs150.
# If the units consumed are more than 400, the cost per unit is 0.90 plus a fixed extra charge of Rs300.
# The function should return the total amount as a float.
# NOTE: This is a function-type question; you only need to complete the function definitionno input reading or printing is required.

# Example

# compute_electricity_bill(200) -> 100.00
# compute_electricity_bill(210) -> 236.50
# compute_electricity_bill(412) -> 670.80
