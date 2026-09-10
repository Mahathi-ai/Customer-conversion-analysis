import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("bank-full.csv",sep=";")
print(df.shape)
print(df.columns)
print(df.isnull().sum())
print(df.duplicated().sum())
df["y"].value_counts().plot(kind="bar")
plt.title("Customer Conversion")
plt.xlabel("Conversion")
plt.ylabel("Number of Customers")
plt.show()
job_conversion=df.groupby("job")["y"].apply(
    lambda x:(x=="yes").mean()*100
)
print(job_conversion)

print("Overall Conversion Rate:", (df["y"] == "yes").mean() * 100)
campaign_conversion = df.groupby("campaign")["y"].apply(
    lambda x: (x == "yes").mean() * 100
)

print(campaign_conversion)