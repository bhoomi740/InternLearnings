import pandas as pd
out = pd.read_csv(r'C:\Users\bhoomika\Downloads\output_file.csv')
recipe = pd.read_excel(r'C:\Users\bhoomika\Downloads\recipe.xlsx')
col1=recipe["Key"].tolist()
col2=recipe["Value"].tolist()
t=out.values.tolist()   #converts all the rows to list
a=t[0]  #initiazing first row of out as a seperate list
b=t[1]  #initiazing second row of out as a seperate list
c=(out.loc[0])   #return row 0
d=(out.loc[[0, 1]])   #return row 0 and 1
e=(out.to_string()) #prints entire data frame
f=(pd.options.display.max_rows) #to check the number of maximum returned rows



