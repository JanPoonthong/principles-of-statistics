import numpy as np
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

x = np.array([53, 59, 65, 78, 82, 79, 84, 77])
y = np.array([156, 167, 173, 178, 189, 194, 171, 185])

slope, intercept, r, p, std_err = stats.linregress(x, y)
print("The regression model is y =", intercept, "+", slope, "*weights")
sns.scatterplot(x, y)
plt.show()
