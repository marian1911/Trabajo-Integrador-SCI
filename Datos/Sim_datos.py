import numpy as np

# Generate 100 evenly spaced PWM values between 0 and 100%
pwm_values = np.linspace(0, 100, 100)

# Simulate temperature values with some realistic assumptions
# Assume a basic quadratic relation where temperature decreases as PWM increases
# Temperature range: 30°C (maximum cooling at 100% PWM) to 90°C (no cooling at 0% PWM)
temp_values = 90 - (pwm_values / 100) * (90 - 30)

# Add some random noise to simulate realistic variations
np.random.seed(42)  # For reproducibility
noise = np.random.normal(0, 2, size=100)  # Small noise with mean=0 and std=2
temp_values += noise

# Combine into a dataset of [PWM, Temperature]
data = np.column_stack((pwm_values, temp_values))
data[:5]  # Show the first 5 rows for reference
