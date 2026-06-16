import requests
import pandas as pd
from pathlib import Path

output_folder = Path(r"C:\Users\dheer\OneDrive\Desktop\project\data\raw")
output_folder.mkdir(parents=True, exist_ok=True)

schemes = {
    "HDFC_Top100": "125497",
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_Large_Cap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841"
}

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        nav_df.to_csv(
            output_folder / f"{name}.csv",
            index=False
        )

        print(f"{name} downloaded successfully")

    else:
        print(f"Failed for {name}")