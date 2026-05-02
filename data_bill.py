# constant values are set here:
TIER_1_DATA_LIMIT_GB = 10
TIER_2_DATA_LIMIT_GB = 20
PREMIUM_USER_OVERAGE_RATE_TIER_2 = 1
REGULAR_USER_OVERAGE_RATE_TIER_2 = 2
PREMIUM_USER_OVERAGE_RATE_TIER_3 = 2
REGULAR_USER_OVERAGE_RATE_TIER_3 = 3



# Your code goes here:

# Welcome message

print("Hi! I am data_bill, I will calculate your phone bill for you. Please respond to prompts below:")

# User Inputs

monthly_data_useage = float(input("Please tell me how much data you have used since your last billing cycle (GB): "))
base_plan_cost = float(input("Please tell me the cost of you plan per month: "))
premium_user = input("Please tell me if you a premium account holder (yes or no): ")

# Boolean for premium

has_premium = premium_user == 'yes' or 'Yes'

# Logic to determine their charges

overage_gb = monthly_data_useage - TIER_1_DATA_LIMIT_GB
overage_rate = 

if has_premium:
    if monthly_data_useage >= TIER_2_DATA_LIMIT_GB:
        overage_cost = overage_gb * PREMIUM_USER_OVERAGE_RATE_TIER_3
        total = base_plan_cost + overage_cost
        overage_rate = PREMIUM_USER_OVERAGE_RATE_TIER_3
    elif monthly_data_useage < TIER_2_DATA_LIMIT_GB and monthly_data_useage >= TIER_1_DATA_LIMIT_GB:
        overage_cost = overage_gb * PREMIUM_USER_OVERAGE_RATE_TIER_2
        total = base_plan_cost + overage_cost
        overage_rate = PREMIUM_USER_OVERAGE_RATE_TIER_3
    else:
        total = base_plan_cost
else:
    if monthly_data_useage >= TIER_2_DATA_LIMIT_GB:
        overage_cost = overage_gb * REGULAR_USER_OVERAGE_RATE_TIER_3
        total = base_plan_cost + overage_cost
        overage_rate = REGULAR_USER_OVERAGE_RATE_TIER_3
    elif monthly_data_useage < TIER_2_DATA_LIMIT_GB and monthly_data_useage >= TIER_1_DATA_LIMIT_GB:
        overage_cost = overage_gb * REGULAR_USER_OVERAGE_RATE_TIER_2
        total = base_plan_cost + overage_cost
        overage_rate = REGULAR_USER_OVERAGE_RATE_TIER_2
    else:
        total = base_plan_cost

# Our Print Statement

if monthly_data_useage > TIER_1_DATA_LIMIT_GB:
    print("You are over your limit by ", overage_gb, " GB.")
    print("Overage rate: $", format(overage_rate, ".02f"), sep = ' ')
    print("Overage cost: $", format(overage_cost, ".02f"), sep = ' ')
    print("Your total bill is $", format(total, ".02f"), sep = ' ')
else:
    print("You are within your data limit.")
    print("Your total bill is $", format(total, ".02f"), sep = ' ')
