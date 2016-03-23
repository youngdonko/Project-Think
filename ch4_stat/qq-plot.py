import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt 


plt. figure()
test_data = np.random.normal(size = 10000)
graph1 =stats.probplot(test_data, dist = "norm", plot=plt)
plt.show()

plt.figure()
test_data2 = np.random.uniform(size = 10000)
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.show()
