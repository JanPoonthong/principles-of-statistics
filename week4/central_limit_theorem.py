import numpy.random as np
import seaborn as sns
import matplotlib.pyplot as plt

population_size = 10000
population = np.random(10000)

number_of_sample = 100
sample_means = np.rand(number_of_sample)
sample_size = 1
c = np.rand(number_of_sample)

for i in range(0, number_of_sample):
    c = np.randint(1, population_size, sample_size)
    sample_means[i] = population[c].mean()

plt.subplot(1, 2, 1)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
sns.displot(sample_means, bins=int(180 / 5), kde=False)
plt.title("Histogram of Sample mean", fontsize=20)
plt.xlabel("Count", fontsize=20)
plt.subplot(1, 2, 2)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
sns.displot(sample_means, kde=True)
plt.title("Density of Sample mean", fontsize=20)
plt.xlabel("Sample mean", fontsize=20)
plt.ylabel("Count", fontsize=20)


plt.show(block=False)
plt.pause(3)
plt.close("all")
