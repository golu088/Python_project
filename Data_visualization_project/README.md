# Documentation for Data Visualization Project

## Project Overview
This Python script provides a simple interface for visualizing data from a CSV file. Users can select columns from the dataset to plot a line chart using the **Matplotlib** library. This tool helps in analyzing relationships between variables in the dataset.

---

## Features
1. **CSV Data Loading**:
   - Reads the contents of a specified CSV file.

2. **User Interaction**:
   - Displays all available columns for user selection.
   - Allows the user to specify columns for the X and Y axes.

3. **Data Visualization**:
   - Plots a line chart of the selected columns with customization options:
     - Grid
     - Title
     - Axis labels

4. **Error Handling**:
   - Handles file not found errors.
   - Ensures valid column selection.
   - Handles unexpected exceptions.

---

## Prerequisites
- Python 3.x
- Required Python libraries:
  - `pandas` (`pip install pandas`)
  - `matplotlib` (`pip install matplotlib`)
- A properly formatted CSV file (e.g., **`emp.csv`**) in the project directory.

---

## Script Walkthrough

### 1. Import Necessary Libraries
```python
import pandas as pd
import matplotlib.pyplot as plt
```
- **`pandas`**: For data loading and manipulation.
- **`matplotlib.pyplot`**: For creating visualizations.

### 2. Define `visualize_data` Function
```python
def visualize_data(file_name):
```
- **Parameters**:
  - `file_name` (str): Name of the CSV file to load.
- **Purpose**:
  - Loads data, allows user column selection, and plots a line chart.

### 3. Load the CSV File
```python
data = pd.read_csv(file_name)
```
- Loads the CSV file into a `pandas` DataFrame.
- Prints the available columns for user reference.

### 4. User Input for Columns
```python
x_column = input("Enter the column name for the X-axis: ")
y_column = input("Enter the column name for the Y-axis: ")
```
- Prompts the user to select columns for the X and Y axes.
- Validates column names against the dataset.

### 5. Plot the Data
```python
plt.figure(figsize=(10, 6))
plt.plot(data[x_column], data[y_column], marker='o', linestyle='-', color='b', label=f'{y_column} vs {x_column}')
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title(f'{y_column} vs {x_column}')
plt.legend()
plt.grid(True)
plt.show()
```
- Creates a line chart with the specified columns.
- Adds labels, title, and grid for clarity.

### 6. Handle Errors
#### FileNotFoundError
```python
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found. Please ensure the file exists.")
```
- Triggers if the specified file is missing.

#### Invalid Columns
```python
if x_column not in data.columns or y_column not in data.columns:
    print(f"Error: One or both of the columns '{x_column}' and '{y_column}' do not exist in the dataset.")
```
- Ensures that both user-specified columns exist in the dataset.

#### General Exceptions
```python
except Exception as e:
    print(f"An error occurred: {e}")
```
- Catches any other unexpected errors.

---

## Example Usage

### Successful Execution
**CSV File**:
```csv
Name,Department,Salary,Age
John Doe,IT,50000,28
Jane Smith,HR,60000,35
Alice Johnson,Finance,55000,30
Bob Brown,IT,60000,40
```

**Input**:
```
Enter the column name for the X-axis: Age
Enter the column name for the Y-axis: Salary
```

**Output**:
A line chart showing the relationship between `Age` (X-axis) and `Salary` (Y-axis).

### Error: Missing CSV File
**Output**:
```
Error: File 'emp.csv' not found. Please ensure the file exists.
```

### Error: Invalid Columns
**Input**:
```
Enter the column name for the X-axis: Experience
Enter the column name for the Y-axis: Salary
```

**Output**:
```
Error: One or both of the columns 'Experience' and 'Salary' do not exist in the dataset.
```

---

## Customizations
1. **Different Plot Types**:
   - Add support for bar charts, scatter plots, etc.
   ```python
   plt.scatter(data[x_column], data[y_column], color='r', label=f'{y_column} vs {x_column}')
   ```

2. **Dynamic File Input**:
   - Allow the user to specify the file name:
   ```python
   file_name = input("Enter the CSV file name: ")
   ```

3. **Save the Plot**:
   - Save the chart as an image:
   ```python
   plt.savefig('plot.png')
   ```

4. **Advanced Visualization**:
   - Use libraries like `seaborn` or `plotly` for more aesthetic and interactive visualizations.

---

## Conclusion
This script provides an interactive and user-friendly tool for visualizing data from CSV files. By leveraging Python libraries, it ensures robustness, simplicity, and extensibility for various use cases.
