Documentation for Salary Data Analysis Project

Project Overview
This project aims to analyze employee salary data using Python and the `pandas` library. The script reads data from a CSV file named **`emp.csv`** and computes statistical measures such as **Mean**, **Median**, and **Mode** of the salary column, provided it exists in the dataset.



 Features
1. **Data Loading**:
   - Reads the CSV file `emp.csv` located in the project directory.
   - Displays all the data from the file for reference.

2. **Salary Analysis**:
   - Verifies the existence of a `Salary` column.
   - Computes the **Mean**, **Median**, and **Mode** of the `Salary` column if present.

3. **Error Handling**:
   - Handles cases where the CSV file is missing (`FileNotFoundError`).
   - Provides a descriptive error message for any unexpected issues.

---

## Prerequisites
- Python 3.x
- `pandas` library installed (`pip install pandas`)
- A properly formatted CSV file named **`emp.csv`** in the project directory.

---

## Required CSV File Structure
The `emp.csv` file should have the following structure:
- One of the columns must be named `Salary`.
- The `Salary` column should contain numerical data.

**Example of `emp.csv`**:
```csv
Name,Department,Salary
John Doe,IT,50000
Jane Smith,HR,60000
Alice Johnson,Finance,55000
Bob Brown,IT,60000
```

---

## Script Walkthrough

### 1. Import Necessary Libraries
```python
import pandas as pd
```
- The `pandas` library is used for data manipulation and analysis.

### 2. Load Data
```python
data = pd.read_csv('emp.csv')
```
- Reads the CSV file into a `pandas` DataFrame. If the file is not found, a `FileNotFoundError` is raised.

### 3. Print the Loaded Data
```python
print(data)
```
- Displays the contents of the CSV file to ensure it is loaded correctly.

### 4. Check for `Salary` Column
```python
if 'Salary' in data.columns:
```
- Ensures the dataset contains a `Salary` column before proceeding with calculations.

### 5. Compute Statistical Measures
```python
mean_salary = data['Salary'].mean()
median_salary = data['Salary'].median()
mode_salary = data['Salary'].mode().iloc[0]
```
- **Mean**: The average salary.
- **Median**: The middle salary value when sorted.
- **Mode**: The most frequently occurring salary.

### 6. Print Results
```python
print(f"Mean: {mean_salary}")
print(f"Median: {median_salary}")
print(f"Mode: {mode_salary}")
```
- Displays the computed statistical measures for the `Salary` column.

### 7. Handle Errors
#### FileNotFoundError
```python
except FileNotFoundError:
    print("Error: CSV file not found. Please ensure the file exists.")
```
- Triggers if the `emp.csv` file is not in the project directory.

#### General Exceptions
```python
except Exception as e:
    print(f"An error occurred: {e}")
```
- Catches and displays any other unexpected errors.

---

## Example Output

### Successful Execution
**CSV File**:
```csv
Name,Department,Salary
John Doe,IT,50000
Jane Smith,HR,60000
Alice Johnson,Finance,55000
Bob Brown,IT,60000
```

**Output**:
```
Data loaded successfully!

           Name Department  Salary
0      John Doe        IT   50000
1    Jane Smith        HR   60000
2  Alice Johnson  Finance   55000
3     Bob Brown        IT   60000

Salary details:
Mean: 56250.0
Median: 57500.0
Mode: 60000
```

### Error: Missing CSV File
**Output**:
```
Error: CSV file not found. Please ensure the file exists.
```

### Error: Missing `Salary` Column
**Output**:
```
Error: 'Salary' column not found in the dataset.
```

---

## Customizations
1. **Adding More Statistical Measures**:
   - Add calculations like standard deviation, variance, etc.
   ```python
   std_salary = data['Salary'].std()
   variance_salary = data['Salary'].var()
   ```

2. **Dynamic File Input**:
   - Modify the script to take the CSV filename as user input.
   ```python
   file_name = input("Enter the CSV file name: ")
   data = pd.read_csv(file_name)
   ```

3. **Data Visualization**:
   - Use libraries like `matplotlib` or `seaborn` to visualize the salary distribution.

---

## Conclusion
This project provides a simple yet effective way to analyze employee salary data. It demonstrates the use of Python for data handling, statistical analysis, and robust error management.
