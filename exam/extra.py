import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# a
x = np.array([4.8, 2.3, 5.6, 4.2, 3.5, 6.4, 8.5, 3.4, 7.1, 6.5])
y = np.array([230, 150, 245, 225, 189, 329, 405, 254, 387, 299])

polynomialorder = 1
model = np.polyfit(x, y, polynomialorder)
modelpredictor = np.polyval(model, x)
absError = modelpredictor - y
SE = np.square(absError)
MSE = np.mean(SE)
print(f"Mean Squared Error: {MSE}")
sns.scatterplot(x, y)
plt.show()

# b
slope, intercept, r, p, std_err = stats.linregress(x, y)
print("The regression model is y =", intercept, "+", slope, "*weights")
sns.scatterplot(x, y)
plt.show()
