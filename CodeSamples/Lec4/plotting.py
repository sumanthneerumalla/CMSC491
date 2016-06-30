import pandas as pd
import matplotlib.pyplot as plt
print "hello"
data = pd.read_csv("http://www.ats.ucla.edu/stat/data/binary.csv",skipinitialspace=True)
print data.head()
print data.mean()
print data.std()
print data.std().index
print data.std().values

print 

print " data to list: "

x = len(data.std().values.tolist())
print x
bucket = 1

print

print "values to list: "
print plt.bar(range(x),data.std().values.tolist(),width=bucket)
print plt.xticks(range(x),data.std().index.tolist())
plt.show()
