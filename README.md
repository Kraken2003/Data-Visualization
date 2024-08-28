## Data Visualization for Economic Comparisons

This repository contains a Python script and Jupyter Notebook designed for analyzing and visualizing economic data from a CSV file. The code enables interactive exploration of economic metrics for two chosen countries, providing a visual comparison of their trends over time.

---

### Project Structure

The repository contains two core files:

- **`Ecnometrics_101.ipynb`:** This Jupyter Notebook serves as the primary driver for the project. It provides a user-friendly interface for loading data, selecting countries and metrics, and generating visualizations.
- **`plotting_function.py`:** This Python script contains the core plotting function (`compare_series`) that handles data transformation and visualization.
  
---

### Functionality

1. **Data Loading and Preprocessing:** 
   - The Jupyter Notebook loads the economic data from a CSV file.
   - It extracts country and series information into dictionaries for convenient lookup.

2. **Interactive Selection:** 
   - The user can interactively choose two countries and an economic metric from the available options.

3. **Visualization:** 
   - The `compare_series` function, called from the Jupyter Notebook, handles data filtering, transformation, and visualization.
   - The function filters the data based on the selected countries and metric, reshapes it for plotting, and uses Seaborn's `lineplot` to generate an interactive line graph.

4. **Customization:** 
   - The generated plot includes labels, a title, a legend, and adjusted x-axis ticks for enhanced readability.
     
---

### Technology Stack

- **Python:** The primary programming language.
- **Jupyter Notebook:** Provides an interactive environment for code execution and visualization.
- **Pandas:** Used for data manipulation and cleaning.
- **Seaborn:** Offers a high-level interface for creating aesthetically pleasing statistical visualizations, including line plots.
- **Matplotlib:** The underlying library for creating static, interactive, and animated visualizations.

---

### Usage Instructions

1. **Install Dependencies:**
   ```bash
   pip install pandas matplotlib seaborn
   ```

2. **Prepare the CSV File:**
   - Create a CSV file containing economic data in the following format:
     - **Country Name:** Name of the country.
     - **Country Code:** Unique code for the country.
     - **Series Name:** Name of the economic metric.
     - **Series Code:** Unique code for the metric.
     - **Years:** Columns representing years (e.g., '2010', '2011', '2012', ...).

3. **Run the Jupyter Notebook:**
   - Open `Ecnometrics_101.ipynb` in a Jupyter Notebook environment.
   - Follow the instructions within the notebook to load the CSV file, select countries and metrics, and generate visualizations.

---

### Code Examples

**`plotting_function.py`:**

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def compare_series(country1_code, country2_code, series_code, df):
    """
    Compares the time series data for two countries based on a specified series code.

    Args:
        country1_code (str): Code of the first country.
        country2_code (str): Code of the second country.
        series_code (str): Code of the economic metric to compare.
        df (pd.DataFrame): DataFrame containing the economic data.

    Returns:
        None (displays the plot)
    """

    # Filter data for the selected countries and series
    filtered_df = df[
        (df["Country Code"] == country1_code) | (df["Country Code"] == country2_code)
    ][["Country Name", "Country Code", "Series Name", "Series Code"] + list(df.columns[5:])]

    # Extract the series name for the plot label
    series_name = filtered_df["Series Name"].unique()[0]

    # Reshape the data into a long format for plotting
    long_df = pd.melt(filtered_df, id_vars=["Country Name", "Country Code"], var_name="Year", value_name="Value")

    # Generate the line plot using Seaborn
    sns.lineplot(x="Year", y="Value", hue="Country Name", data=long_df)
    plt.title(f"Comparison of {series_name} for {country1_code} and {country2_code}")
    plt.xlabel("Year")
    plt.ylabel(series_name)
    plt.xticks(rotation=45)
    plt.legend(title="Country")
    plt.show()

```
---

### Contributing

Contributions to this project are welcome! Please feel free to submit issues or pull requests.

---

### License

This project is licensed under the MIT License.


