import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load your own dataset (replace with the actual path to your dataset)
try:
    # Use read_excel instead of read_csv for .xlsx files
    df = pd.read_excel('Under-five_Deaths_2023.xlsx')

    # Check the first few rows of the dataset
    print("Loaded Data:")
    print(df.head())

except FileNotFoundError:
    print("The file 'Under-five_Deaths_2023.xlsx' was not found. Please check the file path.")
except Exception as e:
    print("An error occurred while loading the data:", e)

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

# Step 3: Visualize the filtered data
try:
    # Line plot for yearly trends between 2019 and 2023
    plt.figure(figsize=(10, 6))
    df_filtered.groupby('Year')['Mortality Rate'].mean().plot(kind='line', marker='o')
    plt.title('Child Mortality Rates (2019-2023)', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Mortality Rate (per 1,000 live births)', fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Heatmap of correlations (if there are additional numerical columns)
    if len(df_filtered.columns) > 2:
        plt.figure(figsize=(8, 6))
        sns.heatmap(df_filtered.corr(), annot=True, cmap="coolwarm", fmt=".2f")
        plt.title('Correlation Matrix (2019-2023)', fontsize=14)
        plt.tight_layout()
        plt.show()
    else:
        print("Not enough numerical columns for a correlation heatmap.")

except Exception as e:
    print("An error occurred while visualizing the filtered data:", e)
