# constant values are set here:
TIER_1_DATA_LIMIT_GB = 10
TIER_2_DATA_LIMIT_GB = 20
PREMIUM_USER_OVERAGE_RATE_TIER_2 = 1
REGULAR_USER_OVERAGE_RATE_TIER_2 = 2
PREMIUM_USER_OVERAGE_RATE_TIER_3 = 2
REGULAR_USER_OVERAGE_RATE_TIER_3 = 3



#/* BELOW PASTED FROM PREVIOUS ASSIGNMENT */
# Data cost constants
DATA_LIMIT = 10
OVERATE_RATE = 2

# User Inputs

user_data_used = float(input("Enter data used (GB): "))
user_base_cost = float(input("Enter base plan cost: $"))

# Process

if user_data_used > DATA_LIMIT:
    print(f"You are over your data limit by {user_data_used - DATA_LIMIT} GB")
    overage_gb = user_data_used - DATA_LIMIT
    if overage_gb > 5:
        print("Extra usage is HIGH")
    else:
        print("Extra usage is MODERATE")
    overage_cost = overage_gb * 2
    print(f"Your total bill is: ${user_base_cost + overage_cost:,.2f}")
else:
    print("You are within the data usage limit")
    print(f"Your total bill is: ${user_base_cost:,.2f}")

#/* ABOVE PASTED FROM PREVIOUS ASSIGNMENT */


    
# Your code goes here: