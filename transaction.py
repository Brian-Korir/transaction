import pandas as pd
df = pd.read_csv('transact.csv')
print(df.head(12))

unit_COUNT = df [(df['unit']=='COUNT')]
unit_COUNT = df [(df['unit']=='DOLLARS')]
#print(len(unit_COUNT.head))
#value_1247 = df [(df['value']=='1247')]
#print(len(value_1247))
unit_COUNT.to_csv('unit-1.csv')