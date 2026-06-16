import pandas as pd
import glob

def ingest_and_validate():
    csv_files = sorted(glob.glob("data/raw/*.csv")) # Ensure your CSVs are in data/raw
    datasets = {}
    
    for f in csv_files:
        df = pd.read_csv(f)
        datasets[f] = df
        print(f"\n--- {f} ---")
        print("Shape:", df.shape)
        print("dtypes:\n", df.dtypes)
        print("Head:\n", df.head(2))
        
    # Explore Fund Master
    fm = datasets.get('data/raw/01_fund_master.csv')
    if fm is not None:
        print("\n--- Fund Master Exploration ---")
        print("Unique Fund Houses:", fm['fund_house'].nunique())
        print("Unique Categories:", fm['category'].unique())
        print("Unique Risk Grades:", fm['risk_category'].unique())
        
    # Validate AMFI Codes
    nav_hist = datasets.get('data/raw/02_nav_history.csv')
    if fm is not None and nav_hist is not None:
        fm_codes = set(fm['amfi_code'])
        nav_codes = set(nav_hist['amfi_code'])
        missing = fm_codes - nav_codes
        print(f"\nTotal codes in fund_master: {len(fm_codes)}")
        print(f"Total codes in nav_history: {len(nav_codes)}")
        print(f"Codes in fund_master missing from nav_history: {len(missing)}")

if __name__ == "__main__":
    ingest_and_validate()