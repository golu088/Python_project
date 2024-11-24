
import pandas as pd

try:
    #csv file also include in my python_project so i can use direct csv file
    data = pd.read_csv('emp.csv') 

     
    print("Data loaded successfully!\n")
    
    print(data) # this print the all the csv data information

    # Check if 'Salary' column exists
    if 'Salary' in data.columns:
        # Calculate Mean, Median, and Mode of Salary column
        mean_salary = data['Salary'].mean()
        median_salary = data['Salary'].median()
        mode_salary = data['Salary'].mode().iloc[0]  

        print("\nsallary details:")
        print(f"Mean: {mean_salary}")
        print(f"Median: {median_salary}")
        print(f"Mode: {mode_salary}")
    else:
        print("Error: 'Salary' column not found in the dataset.")
except FileNotFoundError:
    print("Error: CSV file not found. Please ensure the file exists.")
except Exception as e:
    print(f"An error occurred: {e}")

