import numpy as np
import matplotlib.pyplot as plt

# a
ran = list(range(1, 6, 2))
x = np.random.choice(ran, 100)
y = np.random.choice(ran, 100)

polynomialorder = 1
model = np.polyfit(x, y, polynomialorder)
modelpredictor = np.polyval(model, x)
absError = modelpredictor - y
SE = np.square(absError)
MSE = np.mean(SE)
print(f"Mean Squared Error: {MSE}")

plt.hist(x)
plt.title("X")
plt.show()

plt.hist(x)
plt.title("Y")
plt.show()

plt.hist(MSE)
plt.title("MSE")
plt.show()

# b
import numpy as np
from scipy.stats import linregress

slope, intercept, r, p, std_err = linregress(x, y)
print("the regression model is y = ", intercept, "+ ", slope, "* weight")
