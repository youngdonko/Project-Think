#from scipy import stats
import scipy.stats as stats
import collections
import matplotlib.pyplot as plt 
import pandas as pd 



loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])


plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()


chi, p = stats.chisquare(freq.values())


print (chi)

print (p)