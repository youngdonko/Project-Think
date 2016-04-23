import matplotlib.pyplot as plt 
import pandas as pd 
import scipy.stats as stats 


loansdata = pd.read_csv('loansData.csv')


loansdata.dropna(inplace=True)

loansdata.boxplot(column='Amount.Funded.By.Investors')
plt.show()

loansdata.hist(column='Amount.Funded.By.Investors')
plt.show()


plt.figure()
graph = stats.probplot(loansdata['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.show()
