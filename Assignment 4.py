import numpy as np

# Define the probabilities
P_Rain = 0.3  # Probability of rain
P_NoRain = 1 - P_Rain

P_Accident = 0.1  # Probability of accident
P_NoAccident = 1 - P_Accident

# Conditional probabilities for TrafficJam
P_TrafficJam_given_Rain_Accident = 0.9
P_TrafficJam_given_Rain_NoAccident = 0.6
P_TrafficJam_given_NoRain_Accident = 0.7
P_TrafficJam_given_NoRain_NoAccident = 0.1

# Evidence: It's raining (Rain = 1) and no accident (Accident = 0)
Rain = 1
Accident = 0

# Calculate the probability of TrafficJam given the evidence
if Rain == 1 and Accident == 1:
    P_TrafficJam = P_TrafficJam_given_Rain_Accident
elif Rain == 1 and Accident == 0:
    P_TrafficJam = P_TrafficJam_given_Rain_NoAccident
elif Rain == 0 and Accident == 1:
    P_TrafficJam = P_TrafficJam_given_NoRain_Accident
else:
    P_TrafficJam = P_TrafficJam_given_NoRain_NoAccident

print(f"Probability of TrafficJam given Rain = {Rain} and Accident = {Accident}: {P_TrafficJam}")
