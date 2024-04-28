import numpy as np
import matplotlib.pyplot as plt


# set the random seed
np.random.seed(42)

# set the gaussian parameters as a distribution of price cosumptions
mu = 1000
sigma = 1

# set the number of samples
x_0 = np.random.normal(mu, sigma, 100)
x_1 = np.random.normal(mu, sigma, 1000)
x_2 = np.random.normal(mu, sigma, 10000)

# plot the histogram as normalized
plt.figure()
plt.hist(x_0, bins=30, alpha=0.5, label="100 samples", density=True)
plt.hist(x_1, bins=30, alpha=0.5, label="1000 samples", density=True)
plt.hist(x_2, bins=30, alpha=0.5, label="10000 samples", density=True)
plt.savefig("mean_dynamics/01_01_gaussian_samples.png")

# plot dynamics of the mean
plt.figure()
plt.plot([np.mean(x_2[:i]) for i in range(1, len(x_2))], label="100 samples")
plt.savefig("mean_dynamics/01_02_gaussian_mean.png")
