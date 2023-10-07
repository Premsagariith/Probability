import numpy as np
# Define the number of sides on the die
num_sides = 6

# Probability of getting a 1 on the first roll
prob_1st_roll = 1 / num_sides

# Probability of getting a 4 on the second roll
prob_2nd_roll = 1 / num_sides

# Probability of both events happening (independent events, so we multiply)
probability_both_events = prob_1st_roll * prob_2nd_roll

print("Probability of getting a 1 on the first roll and a 4 on the second roll:", probability_both_events)

