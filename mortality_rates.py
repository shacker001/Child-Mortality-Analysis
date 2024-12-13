import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fetching child mortality data via the World Bank API
url = "https://api.worldbank.org/v2/country/KE/indicator/SH.DYN.MORT"
params = {"format": "json"}  # Specify JSON format

# Step 1: Fetch data from the API
try:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()  # Raise an error for HTTP issues
    data = response.json()

    # Check if data exists in the response
    if data and len(data) > 1 and data[1] is not None:
        records = data[1]
        # Extract relevant fields into a DataFrame
        df = pd.DataFrame.from_records(
            [{"Year": int(entry["date"]), "Mortality Rate": entry["value"]} for entry in records if entry["value"] is not None]
        )
        # Save data to CSV
        df.to_csv('child_mortality_data.csv', index=False)
        print("Data fetched and saved to 'child_mortality_data.csv'.")
    else:
        print("No data available for the requested parameters.")
except requests.exceptions.RequestException as e:
    print("An error occurred while fetching data:", e)

# Step 2: Clean the data and filter for years 2019 to 2023
try:
    # Drop rows with missing data
    df.dropna(inplace=True)

    # Convert Year column to integer (if not already)
    df['Year'] = df['Year'].astype(int)

    # Filter data for the years 2019 to 2023
    df_filtered = df[(df['Year'] >= 2019) & (df['Year'] <= 2023)]

    # Display the cleaned and filtered DataFrame
    print("Filtered Data (2019-2023):")
    print(df_filtered.head())

except Exception as e:
    print("An error occurred while cleaning and filtering the data:", e)

# Step 3: Visualize the data
try:
    # Line plot for yearly trends
    plt.figure(figsize=(10, 6))
    df.groupby('Year')['Mortality Rate'].mean().plot(kind='line', marker='o')
    plt.title('Yearly Trends in Child Mortality Rates in Kenya', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Mortality Rate (per 1,000 live births)', fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Heatmap of correlations (if there are additional numerical columns)
    if len(df.columns) > 2:
        plt.figure(figsize=(8, 6))
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
        plt.title('Correlation Matrix', fontsize=14)
        plt.tight_layout()
        plt.show()
    else:
        print("Not enough numerical columns for a correlation heatmap.")
except Exception as e:
    print("An error occurred while visualizing the data:", e)
