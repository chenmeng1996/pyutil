import pandas as pd

path = "/Users/admin/Desktop/excel"
data = pd.read_excel('123.xls', 'Sheet1', index_col=0)
data.to_csv('data.csv', encoding='utf-8')