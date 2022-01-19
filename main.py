import pandas as pd
out = pd.read_csv(r'C:\Users\bhoomika\Downloads\output_file.csv')
recipe = pd.read_excel(r'C:\Users\bhoomika\Downloads\recipe.xlsx')
#print (out)
#print(recipe.iloc[:])
#keys=recipe.iloc[0:].tolist()
out.drop(["page_num","transaction_num"], axis=1, inplace=True)
row1=out.columns.tolist()
print(row1)
recipe.drop(["Page"], axis=1, inplace=True)
print(recipe)
col1=recipe["Key"].tolist()
print(len(col1))
comp1=[]
for x in row1:
    for y in col1:
        if x == y:
            comp1.append(x)
print(comp1)
print(len(comp1))
print(len(comp1)/len(col1)*100) #this the completion accuracy
##this is the second part##







