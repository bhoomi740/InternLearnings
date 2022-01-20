##selecting and manipulating data##
import pandas as pd
out = pd.read_csv(r'C:\Users\bhoomika\Downloads\output_file.csv')
recipe = pd.read_excel(r'C:\Users\bhoomika\Downloads\recipe.xlsx')
recipe.drop(["Page"], axis=1, inplace=True) #Deleting third column i.e, Page, here axis 1 denotes column
recipe.drop([0,4,165], axis=0, inplace=True) #Deleting 0, 4,165th rows, here axis 0 denots row
col1=recipe["Key"].tolist()
col2=recipe["Value"].tolist()
#print(col1)
print(col2)
t=out.values.tolist()   #converts all the rows to list
a=t[0]  #initiazing firstrow of out as a seperate list
print(a)
##comparing col2 values values with a
elements=[]
for x in col2:
    for y in a:
        if x==y:
          elements.append(x)
print(len(elements))
