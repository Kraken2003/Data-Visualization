## Econometrics 101: Data Visualization with World Bank Data

This repository provides a basic framework for exploring and visualizing economic data from the World Bank. The code utilizes Jupyter Notebook for data loading, analysis, and visualization, while a Python module provides a reusable function for plotting comparisons of time series data.

### Overview

The project consists of three main components:

1. **`Ecnometrics_101.ipynb`**: This Jupyter Notebook acts as the main entry point for the analysis. It defines the workflow, loads data, defines mappings for series and country names, and calls the visualization function to produce plots.
2. **`plotting_function.py`**: This Python module contains the `compare_series` function responsible for creating visualizations. It takes two country codes, a series code, and a DataFrame as input, performs data filtering and reshaping, and generates a line plot using Seaborn.
3. **`world_bank_data.csv`**: This CSV file contains the actual World Bank data, providing various indicators for different countries from 1960 to 2022.

### Installation

1. **Clone the repository:** `git clone https://github.com/[your-username]/Econometrics-101.git`
2. **Create a virtual environment (optional but recommended):**
   - `python3 -m venv .venv`
   - `source .venv/bin/activate`
3. **Install dependencies:** 

### Usage

1. **Open `Ecnometrics_101.ipynb` in Jupyter Notebook.**
2. **Run the cells sequentially to execute the code.**
3. **The notebook will generate a line plot comparing the specified economic indicator between two selected countries.**
4. **Modify the `compare_series` function call in the notebook to analyze different indicators or countries.**
5. **Explore the data further by modifying the notebook or directly accessing the `world_bank_data.csv` file.**

### Working

- The code starts by loading the World Bank data from the `world_bank_data.csv` file into a Pandas DataFrame.
- The `Ecnometrics_101.ipynb` notebook defines dictionaries to map series and country names to their respective codes, facilitating data access.
- The `compare_series` function within `plotting_function.py` performs the following:
    - Filters the DataFrame based on the selected countries and series.
    - Reshapes the data for each country into a "melted" format suitable for line plotting.
    - Creates a line plot using Seaborn, visualizing the data over time for both countries.

### Contributing

Contributions are welcome! Feel free to open issues or pull requests for bug fixes, feature enhancements, or documentation improvements.

### License

This project is licensed under the MIT License. See the `LICENSE` file for details.

### Acknowledgements

This project utilizes the following libraries:

- Pandas
- Seaborn
- Matplotlib

The data used in this project is sourced from the World Bank.
