# import pandas as pd

# print(pd.__version__)

# data = {
#     "Name": ["Ali", "Ahmed", "Jafar"],
#     "Age": [20, 21, 22]
# }

# import pandas as pd

# df=pd.DataFrame({
#     "Name":["Ali","Salah","Gyle"],
#     "Marks":[78,87,66]})

# print(df) 

import pandas as pd
df=pd.read_csv(r"C:\Users\ja773\OneDrive\文档\Ai Engineering\Zomato Restaurant Dataset.csv")

# print(df)
# print(df.head())
# print(df.shape)
# print(df.columns)

# print(df.tail)
# print(df.describe())

# print(df.info())
# print(df["Restaurant Name"])
# print(type(df["Price range"]))

# print(df[["Restaurant Name", "City", "Currency", "Price range"]])
# print(df.iloc[0])
# print(df.dropna())
# print(df.fillna(0))
df.rename(columns={" Restaurant ID":":R_ID"},inplace=True)
print(df)
