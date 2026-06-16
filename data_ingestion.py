from pathlib import Path
import pandas as pd

DATA_PATH = Path(r"C:\Users\dheer\OneDrive\Desktop\project\data\raw")

csv_files = sorted(DATA_PATH.glob("*.csv"))

for file in csv_files:

    print("\n" + "=" * 70)
    print(f"DATASET: {file.name}")

    try:
        df = pd.read_csv(file)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

    except Exception as e:
        print(f"Error: {e}")