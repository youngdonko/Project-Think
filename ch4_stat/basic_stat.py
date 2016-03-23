import pandas as pd 
from scipy import stats

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''


data = data.splitlines()

#data.split('\n')

data = [i.split(',') for i in data]

#print(data[0]) # print headers 

column_names = data[0] # read a header
data_rows = data[1::]

print(column_names)

# Data goes into Padas data frame
df = pd.DataFrame(data_rows, columns = column_names)

# convert it to floating type
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

# Mean
print ( df['Alcohol'].mean() )
print ( df['Tobacco'].mean() )

# Median
print ( df['Alcohol'].median() )
print ( df['Tobacco'].median() )

# Mode
print ( stats.mode(df['Alcohol']))
print ( stats.mode(df['Tobacco']))

# Max-Min
print ( max(df['Alcohol'])-min(df['Alcohol']) )
print ( max(df['Tobacco'])-min(df['Tobacco']) )

# Standard deviation
print ( df['Alcohol'].std() )
print ( df['Tobacco'].std() )

# Variance
print ( df['Alcohol'].var() )
print ( df['Tobacco'].var() )
