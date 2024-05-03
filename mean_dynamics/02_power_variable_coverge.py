import numpy as np
import matplotlib.pyplot as plt


# set the random seed
np.random.seed(42)

# set the log gaussian parameters as a distribution of price cosumptions
mu = 0
sigma = 0.1
scale = 1000

# set the number of samples
x_0 = scale * np.random.lognormal(mu, sigma, 1000)
x_1 = scale * np.random.lognormal(mu, sigma, 10000)
x_2 = scale * np.random.lognormal(mu, sigma, 100000)

# plot the histogram as normalized
fig, ax = plt.subplots()
ax.hist(
    x_0,
    bins=30,
    alpha=0.5,
    label="100 samples",
    density=True,
)
ax.hist(
    x_1,
    bins=30,
    alpha=0.5,
    label="1000 samples",
    density=True,
)
ax.hist(
    x_2,
    bins=30,
    alpha=0.5,
    label="10000 samples",
    density=True,
)
# ax.set_xscale("log")
fig.savefig("mean_dynamics/02_01_log_gaussian_samples.png")

sample_iter = 100

sample_sizes = np.linspace(100, 10000, 100).astype(int)
sample_set = [
    [
        scale * np.random.lognormal(mu, sigma, n)
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
plt.savefig("mean_dynamics/02_02_log_gaussian_mean.png")
