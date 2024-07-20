import numpy as np
import pandas as pd

# Define time array for 365 days
time_days = np.arange(0, 366)  # Time from 0 to 365 days

# Constants for fungal biomass calculation
# These sentinel values can be fine-tuned
carrying_capacity = 10  # Carrying Capacity (K)
growth_rate = 0.1  # Growth Rate (r)
initial_biomass = 1  # Initial fungal biomass (G0)

# Constants for radiation level calculation
initial_radiation_level = 1000  # Initial radiation level (R0)
decontamination_rate_constant = 0.05  # Decontamination rate constant (k)

# Specific constant for another calculation
specific_constant = 114.1475309
H2 = 0.05  # Example constant (H2)

# Calculate fungal biomass using the logistic growth model
fungal_biomass = carrying_capacity / (1 + ((carrying_capacity - initial_biomass) / initial_biomass) * np.exp(-growth_rate * time_days))

# Calculate radiation level using the first-order kinetics model
radiation_level = initial_radiation_level * np.exp(-decontamination_rate_constant * time_days)

# Calculate the value using the given formula with the specific constant value
specific_result = specific_constant * np.exp(-H2 * time_days)

# Create a DataFrame to store the results
data = {
    "Time (days)": time_days,
    "Fungal Biomass": fungal_biomass,
    "Radiation Level": radiation_level,
    "Specific Result": specific_result
}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
file_path = "simulation_results_365_days.csv"
df.to_csv(file_path, index=False)

print(f"Results saved to {file_path}")
