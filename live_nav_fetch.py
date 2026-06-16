import requests
import pandas as pd
import time

def fetch_nav(amfi_code):
    url = f"https://api.mfapi.in/mf/{amfi_code}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # The API returns 'meta' and 'data'. We'll extract the latest NAV.
        if 'data' in data and len(data['data']) > 0:
            latest_nav = data['data'][0]
            return {
                'amfi_code': amfi_code,
                'scheme_name': data.get('meta', {}).get('scheme_name', 'Unknown'),
                'date': latest_nav.get('date'),
                'nav': latest_nav.get('nav')
            }
    except Exception as e:
        print(f"Failed to fetch {amfi_code}: {e}")
    return None

def main():
    schemes = [125497, 119551, 120503, 118632, 119092, 120841]
    results = []
    
    print("Fetching live NAV data...")
    for code in schemes:
        nav_data = fetch_nav(code)
        if nav_data:
            results.append(nav_data)
        time.sleep(0.5) # Be polite to the API
        
    if results:
        df = pd.DataFrame(results)
        print("\nFetched Data:")
        print(df)
        
        # Save as raw CSV
        output_path = "data/raw/live_nav_updates.csv"
        df.to_csv(output_path, index=False)
        print(f"\nSaved live NAVs to {output_path}")

if __name__ == "__main__":
    main()