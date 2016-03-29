import pandas as pd
import matplotlib.pyplot as plt

'''
4 line code for comprehensive
'''

#import pandas as pd
#read data into dataframe
#loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

##remove % symbol from interest rate and convert to float
#loansData['Interest.Rate'] = [float(interest[0:-1])/100 for interest in loansData['Interest.Rate']]

##remove "month" at the end of loan length and convert to integer
#loansData['Loan.Length'] = [int(length[0:-7]) for length in loansData['Loan.Length']]

##create a new column called Fico Score with lower limit value
#loansData['FICO.Score'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']]
##


loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')


a = loansData['Interest.Rate'][0:5].values[1]
#a = a.rstrip('%')
#a = float(a)
#a = a/100
#a = round(a,4)

# lambda function
#b = lambda a: round(float(a.rstrip('%'))/100,4)

cleanInterestRate = loansData['Interest.Rate'].map(lambda a:round(float(a.rstrip('%'))/100,4))

loansData['Interest.Rate']=cleanInterestRate

b = loansData['Loan.Length'][0:5].values[1]

cleanLoanLength = loansData['Loan.Length'].map(lambda a:round(float(a.strip('months'))))
loansData['Loan.Length'] = cleanLoanLength

c = loansData['FICO.Range'][0:5].values[1]
#cleanFICORange = loansData['FICO.Range'].map(lambda a:a.split('-'))
#cleanFICORange = cleanFICORange.map(lambda a:[int(n[:3]) for n in a])
#loansData['FICO.Score'] = cleanFICORange

loansData['FICO.Score'] = loansData['FICO.Range'].map(lambda x: int(x[:3]))

plt.figure()
p = loansData['FICO.Score'].hist()
plt.show()

aa = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal = 'hist')
