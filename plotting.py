import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Reading the file
df = pd.read_excel('GDP_and_Major_Industrial_Sectors_of_Economy_Dataset.xls')
df.dropna(inplace=True)
# print(df.head())
x = df['Financial Year'].tolist()
df = df.select_dtypes(include = ['float64', 'int64'])

length = len(df.columns)
cols = df.columns
# print(length)
n_cols = 4
n_rows = int(length/n_cols)

#Scatter Plot

fig1 = plt.figure(figsize=(20,10))
col1 = 'Gross Domestic Product - % Growth Rate (YoY)'
col2 = 'Mining and Quarrying - % Growth Rate (YoY)'
col3 = 'Services - % Growth Rate (YoY)'

plt.scatter(x=np.arange(1,62,1), y=df[col1].tolist(), label = col1, alpha = 0.6, color = 'r')
plt.scatter(x=np.arange(1,62,1), y=df[col2].tolist(), label = col2, alpha = 0.6, color = 'blue')
plt.scatter(x=np.arange(1,62,1), y=df[col3].tolist(), label = col3, alpha = 0.6, color = 'g')
plt.ylabel('Percentage Growth', fontsize=15)
plt.xticks(np.arange(1,62,1), x, rotation=45)
plt.xlabel('Financial Year' , fontsize=15)
plt.title('Scatter Plot of various percentage growth w.r.t Financial Year', fontsize=15)
plt.legend()
# plt.show()
fig1.savefig('Scatter_Plot.jpg', dpi=300)

#Box Plot

fig2 = plt.figure(figsize=(20,15))
columns = []
for i in cols[13:]:
    columns.append(i)
length = len(columns)
# print(columns)
df.boxplot(column = columns, fontsize=10)
plt.ylabel('Percentage Growth', fontsize=15)
plt.xticks(rotation=45)
# plt.xlabel(fontsize=15)
# plt.legend()
plt.title('Box Plot of various percentage growth w.r.t Financial Year', fontsize=15)
# plt.show()
plt.tight_layout()
fig2.savefig('Box_Plot.jpg', dpi=300)

#Line Plot
fig3 = plt.figure(figsize=(20,10))
col1 = 'Agri-culture & Allied Services - % Growth Rate (YoY)'
col2 = 'Industry - % Growth Rate (YoY)'
col3 = 'Manufacturing - % Growth Rate (YoY)'

plt.plot(np.arange(1,62,1), df[col1].tolist(), label = col1, alpha = 0.5, color = 'r', marker='o', markersize=6)
plt.plot(np.arange(1,62,1), df[col2].tolist(), label = col2, alpha = 0.5, color = 'blue', marker='v', markersize=6)
plt.plot(np.arange(1,62,1), df[col3].tolist(), label = col3, alpha = 0.5, color = 'black', marker='d', markersize=6)
plt.ylabel('Percentage Growth', fontsize=15)
plt.xticks(np.arange(1,62,1), x, rotation=45)
plt.xlabel('Financial Year' , fontsize=15)
plt.title('Scatter Plot of various percentage growth w.r.t Financial Year', fontsize=15)
plt.legend()
# plt.show()
fig3.savefig('Line_Plot.jpg', dpi=300)