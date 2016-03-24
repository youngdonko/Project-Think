import matplotlib.pyplot as plt 
import scipy.stats as stats
import pandas as pd 


loansdata = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

loansdata.dropna(inplace=True)

loansdata.boxplot(column='Amount.Requested')
plt.show()

loansdata.hist(column='Amount.Requested')
plt.show()

plt.figure()
graph = stats.probplot(loansdata['Amount.Requested'], dist="norm", plot=plt)
plt.show()
