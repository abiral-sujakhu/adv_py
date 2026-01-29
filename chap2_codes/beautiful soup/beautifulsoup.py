import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

print("=" * 70)
print("🌍 GDP DATA SCRAPER - Country-wise GDP Extraction")
print("=" * 70)

# URL with GDP data (Wikipedia's List of Countries by GDP)
url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

print(f"\n📡 Fetching data from: {url}")

try:
    # Send request to the website
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    print("✓ Data fetched successfully!")
    
    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(response.content, 'lxml')
    
    print("✓ HTML parsed successfully!")
    print("\n🔍 Extracting GDP data...")
    
    # Find the main GDP table (usually the first major table)
    # Looking for table with class 'wikitable'
    tables = soup.find_all('table', {'class': 'wikitable'})
    
    if not tables:
        print("❌ No tables found!")
        exit()
    
    # Use the first table which contains IMF data
    table = tables[0]
    
    # Extract data
    gdp_data = []
    
    # Get table headers
    headers_row = table.find('tr')
    headers = [th.get_text(strip=True) for th in headers_row.find_all('th')]
    
    print(f"✓ Found table with columns: {', '.join(headers[:4])}")
    
    # Extract rows
    rows = table.find_all('tr')[1:]  # Skip header row
    
    for row in rows:
        cols = row.find_all(['td', 'th'])
        
        if len(cols) >= 3:  # Ensure row has enough columns
            # Extract rank, country, and GDP
            rank = cols[0].get_text(strip=True)
            country = cols[1].get_text(strip=True)
            gdp = cols[2].get_text(strip=True)
            
            # Clean the data
            if rank and country and gdp:
                gdp_data.append({
                    'Rank': rank,
                    'Country': country,
                    'GDP (millions USD)': gdp
                })
    
    print(f"✓ Extracted {len(gdp_data)} countries!")
    
    # Save to CSV using csv module
    csv_filename = 'gdp_countries.csv'
    
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        if gdp_data:
            fieldnames = ['Rank', 'Country', 'GDP (millions USD)']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(gdp_data)
    
    print(f"\n✅ Data saved to: {csv_filename}")
    
    # Display first 10 countries
    print("\n" + "=" * 70)
    print("📊 TOP 10 COUNTRIES BY GDP:")
    print("=" * 70)
    
    for i, data in enumerate(gdp_data[:10], 1):
        print(f"{data['Rank']:>3}. {data['Country']:<30} ${data['GDP (millions USD)']}")
    
    # Also create a pandas DataFrame and save as CSV
    df = pd.DataFrame(gdp_data)
    pandas_csv = 'gdp_countries_pandas.csv'
    df.to_csv(pandas_csv, index=False, encoding='utf-8')
    
    print(f"\n✅ Also saved using pandas to: {pandas_csv}")
    
    # Display statistics
    print("\n" + "=" * 70)
    print("📈 STATISTICS:")
    print("=" * 70)
    print(f"Total countries extracted: {len(gdp_data)}")
    print(f"CSV file size: {len(gdp_data)} rows")
    
except requests.exceptions.RequestException as e:
    print(f"❌ Error fetching data: {e}")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 70)
