import numpy as np
import matplotlib.pyplot as plt

# Simulated data
true_values = np.array([1, 2, 3, 4, 5])
predicted_values = np.array([0.8, 2.2, 3.2, 4.5, 5.3])

# Calculate errors
errors = np.fabs(true_values - predicted_values)

# Plotting
plt.figure(figsize=(8, 6))
plt.errorbar(true_values, predicted_values, yerr=errors, fmt='o', label='Fitting Result')
plt.plot(true_values, true_values, 'r--', label='Ideal Fit')
plt.xlabel('True Values')
plt.ylabel('Predicted Values')
plt.title('Fitting Result with Error Bars')
plt.legend()
plt.grid(True)
plt.show()