import pandas as pd
import sqlite3
import os

# File paths
data_folder = "data"
files = {
    "ad_sales_metrics": os.path.join(data_folder, "ad_sales_metrics.csv"),
    "total_sales_metrics": os.path.join(data_folder, "total_sales_metrics.csv"),
    "eligibility_table": os.path.join(data_folder, "eligibility_table.csv")
}

# Load and insert into DB
conn = sqlite3.connect("ecommerce.db")

for table_name, path in files.items():
    df = pd.read_csv(path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"✅ Loaded {table_name} into database.")

conn.close()
print("✅ All data loaded into ecommerce.db")
