# Fuel Price Analysis - Brazil (2024)

![Status](https://img.shields.io/badge/Status-Completed-green)  ![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## About the Project
This project analyzes and extracts relevant information from a government-provided dataset on the main fuels used in Brazil during the first half of 2024. The system processes the dataset to generate visualizations of price trends by state, highlighting price variations and identifying states with the highest and lowest fuel prices.

## :hammer: Features

- **Data Processing**:  
  Reads and processes the dataset (`Precos.csv`) containing fuel price information.
  Filters data based on fuel type and state.
  Implements **Timsort** and **Merge Sort** algorithms to efficiently sort price data.

- **Price Analysis**:  
  - `Maximum Price`: Identifies the highest fuel price per state.
  - `Minimum Price`: Identifies the lowest fuel price per state.
  - `Average Price`: Computes the mean fuel price per state.
  - `Price Variability`: Determines states with the highest and lowest price variations.

- 📈 **Data Visualization**:  
  - Generates **Matplotlib** graphs to visualize fuel price trends per state.
  - Highlights maximum, minimum, and average prices with distinct markers and colors.

## ✅ Technologies Used

- **Pandas**: Data handling and filtering
- **Matplotlib**: Graph and visualization generation
- **Timsort & Merge Sort**: Efficient sorting algorithms for processing price data

## How It Works

1. The dataset is loaded from `Precos.csv`.
2. The user selects a fuel type.
3. The system extracts price data for each Brazilian state.
4. The data is sorted and analyzed.
5. A graph is generated to visualize price trends.
6. The system prints the lowest five prices per state.

## Example Output

- A line chart displaying maximum, minimum, and average fuel prices per state.
- Sorted price data for further analysis.

## Usage

To run the analysis, execute the script in a Python environment with Pandas and Matplotlib installed and the csv archive in the same folder as the code.

```bash
python fuel_analysis.py
```

