import numpy as np
import matplotlib.pyplot as plt


# set the random seed
np.random.seed(42)

# set the gaussian parameters as a distribution of price cosumptions
mu = 1000
sigma = 1

# set the number of samples
x_0 = np.random.normal(mu, sigma, 1000)
x_1 = np.random.normal(mu, sigma, 10000)
x_2 = np.random.normal(mu, sigma, 100000)

# plot the histogram as normalized
plt.figure()
plt.hist(x_0, bins=30, alpha=0.5, label="100 samples", density=True)
plt.hist(x_1, bins=30, alpha=0.5, label="1000 samples", density=True)
plt.hist(x_2, bins=30, alpha=0.5, label="10000 samples", density=True)
plt.savefig("mean_dynamics/01_01_gaussian_samples.png")

sample_iter = 100

sample_sizes = np.linspace(10, 10000, 100).astype(int)
sample_set = [
    [
        np.random.normal(mu, sigma, n)
        for _ in range(sample_iter)
    ] for n in sample_sizes
]  # fmt: skip
means_set = np.array(
    [[np.mean(sample) for sample in sample_set] for sample_set in sample_set]
)
means = np.array([np.mean(means) for means in means_set])
stds = np.array([np.std(means) for means in means_set])

# plot dynamics of the mean
plt.figure()
plt.plot(sample_sizes, means, label="mean")
plt.fill_between(
    sample_sizes,
    means - stds,
    means + stds,
    alpha=0.5,
    label="std",
)
plt.savefig("mean_dynamics/01_02_gaussian_mean.png")
