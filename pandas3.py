import pandas as pd
out = pd.read_csv(r'C:\Users\bhoomika\Downloads\output_file.csv')
recipe = pd.read_excel(r'C:\Users\bhoomika\Downloads\recipe.xlsx')
col1=recipe["Key"].tolist()
col2=recipe["Value"].tolist()
#print(col1)
#To alter the values
col2[4]="CALIFORNIA"
col2[6:8]="s","y","p"
a=col2[0:12]  #print specific values
b=a.append("Mysuru")
print(col2)
print(a)

