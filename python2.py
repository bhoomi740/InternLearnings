import pandas as pd
out = pd.read_csv(r'C:\Users\bhoomika\Downloads\output_file.csv')
recipe = pd.read_excel(r'C:\Users\bhoomika\Downloads\recipe.xlsx')
# converting to dictionary
out.dropna(inplace=True)
out_dict=out.to_dict('series')
print(type(out_dict['price'])
print(out_dict)
