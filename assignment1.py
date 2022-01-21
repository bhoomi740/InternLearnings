import pandas as pd
out = pd.read_csv(r'C:\Users\bhoomika\Downloads\output_file.csv')
recipe = pd.read_excel(r'C:\Users\bhoomika\Downloads\recipe.xlsx')
out.drop(["page_num","transaction_num"], axis=1, inplace=True)
row1=out.columns.tolist()   #print(row1)
recipe.drop(["Page"], axis=1, inplace=True)     #print(recipe)
col1=recipe["Key"].tolist()     #print(len(col1))
col2=recipe["Value"].tolist()

##________completion accuracy_____________##
comp1=[]
for x in row1:
    for y in col1:
        if x == y:
            comp1.append(x)     #print(comp1) #print(len(comp1))
print(len(comp1)/len(col1)*100)     #this the completion accuracy

##________Correctness accuracy ___________##

t=out.values.tolist()   #converts all the rows to list #print(t)
a=t[0]  #initiazing first row of out as a seperate list
b=t[1]  #initiazing second row of out as a seperate list #print(a) #print(len(a)) #print(b)

value1=[]
for k in a:
    for l in col2[0:83]:
        if k==l:
            #print(k)
            value1.append(k)
v1=len(value1)
#print(v1)
print(v1/len(col2[0:83])*100)

value2=[]
for m in b:
    for n in col2[83:167]:
        if m==n:
            value2.append(m)
v2=len(value2)
#print(v2)
print(v2/len(col2[83:167])*100)     #print(v2/len(comp1)*100)


