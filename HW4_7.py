from scipy.stats import t
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate 100 random numbers from t-distribution with df=10
deg_of_freedom = 10  # degrees of freedom
rand_num = t.rvs(deg_of_freedom, size=100)

# Step 2: Calculate mean μ and standard deviation σ of these numbers
mean= np.mean(rand_num)
stdev= np.std(rand_num)

# Step 3: Create 15 sampling groups, each with 30 samples
num_samples = 30
num_groups = 15
sampling_group_means = []

for _ in range(num_groups):
    sample = np.random.choice(rand_num, size=num_samples, replace=False)
    sampling_group_means.append(np.mean(sample))

# Step 4: Calculate the mean of the sampling group means
mean_of_means = np.mean(sampling_group_means)

# Step 5: Verify CLT
# The standard deviation of the sample means (σx) should be close to σ/√n
sigma_x = np.std(sampling_group_means)
expected_sigma_x = stdev/ np.sqrt(num_samples)

# Step 6: Plot histogram of the sample means
plt.hist(sampling_group_means, bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.xlabel('Sample Means')
plt.ylabel('Frequency')
plt.title('Histogram of Sample Means')
plt.show()

print(mean, stdev, mean_of_means, sigma_x, expected_sigma_x)
