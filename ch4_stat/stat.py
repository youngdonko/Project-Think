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

data = [i.split(',') for i in data]

column_names = data[0]
data_rows = data[1::]

df = pd.DataFrame(data_rows, columns = column_names)


df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

a1 = df['Alcohol'].mean()
a2 = df['Alcohol'].median()
a3 = stats.mode(df['Alcohol'])
a4 = df['Alcohol'].var()
a5 = df['Alcohol'].std()


print ("The mean of Alcohol is %f" %a1 )
print ("The median of Alcohol is %f" %a1)
print ("The mode of Alcohol is %r" %a3[0])
print ("The variance of Alcohol is %f" %a4)
print ("The standard deviation of Alcohol is %f" %a5)


b1 = df['Tobacco'].mean()
b2 = df['Tobacco'].median()
b3 = stats.mode(df['Tobacco'])
b4 = df['Tobacco'].var()
b5 = df['Tobacco'].std()

print ("The mean of Tobacco is %f" %b1)
print ("The median of Tobacco is %f" %b2)
print ("The mode of Tobacco is %r" %b3[0])
print ("The variance of Tobacco is %f" %b4)
print ("The standard deviation of Tobacco is %f" %b5)


ab1 = max(df['Alcohol'])-min(df['Alcohol'])
ab2 = max(df['Tobacco'])-min(df['Tobacco'])
print ("The range of Alcohol is %f" %ab1)
print ("The range of Tobacco is %f" %ab2)



