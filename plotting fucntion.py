import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def compare_series(country_code1, country_code2, series_code, df):
    """
    Compare two countries' data for a specific series over time using line plots.

    Args:
        country_code1 (str): Country code of the first country.
        country_code2 (str): Country code of the second country.
        series_code (str): Series code for the data to be compared.
        df (pd.DataFrame): DataFrame containing the data.

    Returns:
        None (displays a line plot comparing the two countries' data).
    """
    # Filter data for the specified countries and series
    country1_data = df[(df['Country Code'] == country_code1) & (df['Series Code'] == series_code)]
    country2_data = df[(df['Country Code'] == country_code2) & (df['Series Code'] == series_code)]

    # Extract the series name from one of the dataframes
    series_name = country1_data['Series Name'].iloc[0]

    # Reshape the data to a melted format for visualization
    country1_data_melted = country1_data.melt(id_vars=['Country Name'], value_vars=df.columns[4:], var_name='Year', value_name=series_name)
    country2_data_melted = country2_data.melt(id_vars=['Country Name'], value_vars=df.columns[4:], var_name='Year', value_name=series_name)

    # Create a line plot
    plt.figure(figsize=(12, 6))
    sns.set_theme(style='darkgrid')
    
    # Plot the data for the first country in red
    sns.lineplot(data=country1_data_melted, x='Year', y=series_name, hue='Country Name', palette=['red'])
    
    # Plot the data for the second country in blue
    sns.lineplot(data=country2_data_melted, x='Year', y=series_name, hue='Country Name', palette=['blue'])

    # Set plot attributes
    plt.title(f'{series_name} Comparison: {country_code1} vs {country_code2}')
    plt.xlabel('Year')
    plt.ylabel(series_name)
    plt.legend(title='Country Name')
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))
    
    # Display the plot
    plt.show()

# Example usage
# compare_series("USA", "CAN", "GDP", df)  # Replace with actual country codes, series code, and DataFrame
