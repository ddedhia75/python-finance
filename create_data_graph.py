import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


df = pd.read_csv('spy.csv', parse_dates=True, index_col=0)

#print(df.head())


#df['Adj Close'].plot()
#df[['High', 'Low']].plot()
#plt.show()
#plt.savefig("spy.png")



#df['50ma'] = df['Adj Close'].rolling(window=50).mean()

df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

#df[['50ma','100ma']].plot()

#plt.show()

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1,sharex=ax1)


ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

plt.show()
