import pandas as pd
import sqlite3

df = pd.read_csv("../data/raw/sales_90_days.csv")

print("\nDataset shape:")
print(df.shape)

print("\nDataset columns:")
print(df.columns.tolist())

print("\nFirst five rows:")
print(df.head(5))

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

missing_product_type = df[df["product_type"].isna()]
print("\nRows with Missing Product Type:")
print(missing_product_type)

df["product_type"] = df["product_type"].fillna("Miscellaneous")
print("\nRows with Missing Product Type:")
print(df["product_type"].value_counts())

df.to_csv("../data/processed/sales_90_days.csv", index=False)