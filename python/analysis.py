import pandas as pd
import sqlite3

conn = sqlite3.connect("../data/processed/sales_90_days_clean.db")


def load_sql(filename):
    with open(f"../sql/{filename}", "r") as file:
        return file.read()


def run_query(filename):
    query = load_sql(filename)
    return pd.read_sql_query(query, conn)

# product performance query
product_performance = run_query("product_performance.sql")

print("\n=== PRODUCT PERFORMANCE ===")
print(product_performance)

# vendor performance
vendor_performance = run_query("vendor_performance.sql")

print("\n=== VENDOR PERFORMANCE ===")
print(vendor_performance)

# product type performance
product_type = run_query("product_type_performance.sql")
print("\n=== PRODUCT TYPE PERFORMANCE ===")
print(product_type)

# discounts and reversals
discount_reversal = run_query("discount_and_reversals.sql")
print("\n=== DISCOUNT & REVERSAL ANALYSIS ===")
print(discount_reversal)

# high and low performers
high_low_performers = run_query("high_low_performers.sql")
print("\n=== HIGH & LOW PERFORMERS ===")
print(high_low_performers)

# stats
median_sales = product_performance["net_sales"].median()
mean_sales = product_performance["net_sales"].mean()
std_sales = product_performance["net_sales"].std()

print("Mean net sales:", round(mean_sales, 2))
print("Median net sales:", round(median_sales, 2))
print("Standard deviation:", round(std_sales, 2))

Q1 = product_performance["net_sales"].quantile(0.25)
Q3 = product_performance["net_sales"].quantile(0.75)

print("Q1 Net Sales:", round(Q1, 2))
print("Q3 Net Sales:", round(Q3, 2))

IQR = Q3 - Q1

outliers = product_performance[
    (product_performance["net_sales"] < Q1 - 1.5 * IQR) |
    (product_performance["net_sales"] > Q3 + 1.5 * IQR)
]

print("\nSales Outliers:")
print(outliers)