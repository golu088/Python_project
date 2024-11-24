
import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(file_name):
    try:
        # Load CSV data
        data = pd.read_csv('emp.csv')
        print("Data loaded successfully!")
        print("\nAvailable columns in the dataset:")
        print(data.columns.tolist())

        # select the x_column and y_column for data visualization
        x_column = input("Enter the column name for the X-axis: ")
        y_column = input("Enter the column name for the Y-axis: ")

        if x_column not in data.columns or y_column not in data.columns:
            print(f"Error: One or both of the columns '{x_column}' and '{y_column}' do not exist in the dataset.")
            return

        # plot the data for visualization
        plt.figure(figsize=(10, 6))
        plt.plot(data[x_column], data[y_column], marker='o', linestyle='-', color='b', label=f'{y_column} vs {x_column}')
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title(f'{y_column} vs {x_column}')
        plt.legend()
        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found. Please ensure the file exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # File name of the CSV (emp)
    file_name = 'emp.csv'
    visualize_data(file_name)


