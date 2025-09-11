import pandas

df = pandas.read_csv("C:\\Users\\aleja\\Desktop\\Book1.csv")
df = df.drop(["Spanish"])
print(df)
# df = df.to_dict(orient='records')
# print(df)