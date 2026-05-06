# constant values are set here:
TIER_1_DATA_LIMIT_GB = 10
TIER_2_DATA_LIMIT_GB = 20
PREMIUM_USER_OVERAGE_RATE_TIER_2 = 1
REGULAR_USER_OVERAGE_RATE_TIER_2 = 2
PREMIUM_USER_OVERAGE_RATE_TIER_3 = 2
REGULAR_USER_OVERAGE_RATE_TIER_3 = 3


# Data cost constants
DATA_LIMIT = 10
OVERAGE_RATE = 2

# User Inputs

user_data_used = float(input("Enter data used (GB): "))
user_base_cost = float(input("Enter base monthly plan cost: $"))
user_premium_status = input("Are you a premium user? (yes/no): ")

DATA_USED = user_data_used
PREMIUM_STATUS = user_premium_status
BASE_COST = user_base_cost

# Process

if user_data_used <= TIER_1_DATA_LIMIT_GB:
    overage_cost = 0
    print("You are within the data usage limit")
    print(f"GB over limit: 0")
    print(f"Your overage cost is: ${overage_cost:,.2f}")
    print(f"Your total bill is: ${BASE_COST + overage_cost:,.2f}")

# More than 10 GB used but not more than 20 GB
elif user_data_used <= TIER_2_DATA_LIMIT_GB:
    if PREMIUM_STATUS == "yes":
        overage_cost = float((DATA_USED - TIER_1_DATA_LIMIT_GB) * PREMIUM_USER_OVERAGE_RATE_TIER_2)
        print(f"You are {DATA_USED - TIER_1_DATA_LIMIT_GB:,.1f} GB over your data usage limit")
        print(f"Your overage rate is: ${PREMIUM_USER_OVERAGE_RATE_TIER_2:,.2f} per GB")
        print(f"Your overage cost is: ${overage_cost:,.2f}")
        print(f"Your total bill is: ${BASE_COST + overage_cost:,.2f}")
    else:        
        overage_cost = float((DATA_USED - TIER_1_DATA_LIMIT_GB) * REGULAR_USER_OVERAGE_RATE_TIER_2)
        print(f"You are {DATA_USED - TIER_1_DATA_LIMIT_GB:,.1f} GB over your data usage limit")
        print(f"Your overage rate is: ${REGULAR_USER_OVERAGE_RATE_TIER_2:,.2f} per GB")
        print(f"Your overage cost is: ${overage_cost:,.2f}")
        print(f"Your total bill is: ${BASE_COST + overage_cost:,.2f}")

# More than 20 GB used
elif user_data_used > TIER_2_DATA_LIMIT_GB:
    if PREMIUM_STATUS == "yes":
        overage_cost = float((TIER_2_DATA_LIMIT_GB - TIER_1_DATA_LIMIT_GB) * PREMIUM_USER_OVERAGE_RATE_TIER_2 + \
                             (DATA_USED - TIER_2_DATA_LIMIT_GB) * PREMIUM_USER_OVERAGE_RATE_TIER_3)
        print(f"You are {DATA_USED - TIER_1_DATA_LIMIT_GB:,.1f} GB over your data usage limit")
        print(f"Your overage rate is: ${PREMIUM_USER_OVERAGE_RATE_TIER_3:,.2f} per GB")
        print(f"Your overage cost is: ${overage_cost:,.2f}")
        print(f"Your total bill is: ${BASE_COST + overage_cost:,.2f}")
    else:
        overage_cost = float((TIER_2_DATA_LIMIT_GB - TIER_1_DATA_LIMIT_GB) * REGULAR_USER_OVERAGE_RATE_TIER_2 + \
                             (DATA_USED - TIER_2_DATA_LIMIT_GB) * REGULAR_USER_OVERAGE_RATE_TIER_3)
        print(f"You are {DATA_USED - TIER_1_DATA_LIMIT_GB:,.1f} GB over your data usage limit")
        print(f"Your overage rate is: ${REGULAR_USER_OVERAGE_RATE_TIER_3:,.2f} per GB")
        print(f"Your overage cost is: ${overage_cost:,.2f}")
        print(f"Your total bill is: ${BASE_COST + overage_cost:,.2f}")
else:
    print("***ERROR TRY AGAIN***")


## OLD CODE -- Assignment 1 code for reference

#if user_data_used > DATA_LIMIT:
#    print(f"You are over your data limit by {user_data_used - DATA_LIMIT} GB")
#    overage_gb = user_data_used - DATA_LIMIT
#    if overage_gb > 5:
#        print("Extra usage is HIGH")
#    else:
#        print("Extra usage is MODERATE")
#    overage_cost = overage_gb * 2
#    print(f"Your total bill is: ${user_base_cost + overage_cost:,.2f}")
#else:
#    print("You are within the data usage limit")
#    print(f"Your total bill is: ${user_base_cost:,.2f}")"""

# Your code goes here: