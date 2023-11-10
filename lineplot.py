import pandas as pd
import matplotlib.pyplot as plt

# Define a function to create a line plot
def create_line_plot(data, x_values, y_values, labels, colors, title, x_label, y_label, save_path):
    # Create a new figure for the plot with a specified size (10 units wide and 6 units high)
    plt.figure(figsize=(10, 6))

    # Add 100,000 to each value in the 'Deaths' and 'Recovered' columns
    data[y_values] = data[y_values] + 100000
    
    # Loop through each y_value (e.g., 'Deaths', 'Recovered') and plot the data
    for i in range(len(y_values)):
        plt.plot(x_values, data[y_values[i]], label=labels[i], color=colors[i])

    # Set the title, x-axis label, and y-axis label for the plot
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Display grid lines on the plot
    plt.grid(True)

    # Calculate and display maximum values for each data series
    for i in range(len(y_values)):
        max_value = data[y_values[i]].max()
        max_date = x_values[data[y_values[i]].idxmax()]
        plt.annotate(f"Total: {max_value}\nDate: {max_date.strftime('%Y-%m-%d')}", xy=(max_date, max_value), xytext=(20, -20), textcoords='offset points', arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=0.5"))

    # Add a legend to the plot based on the provided labels
    plt.legend()

    # Ensure a tight layout to prevent labels from getting cut off
    plt.tight_layout()

    # Save the plot as a PNG image with the specified file path
    plt.savefig(save_path)

    # Show the plot on the screen
    plt.show()

    # Return from the function
    return

# Load the data from the CSV file (replace 'your_data.csv' with your actual file path)
data = pd.read_csv('day_wise.csv')

# Convert the 'Date' column to a datetime object for easier manipulation
data['Date'] = pd.to_datetime(data['Date'])

# Define the x-values (dates) based on the 'Date' column
x_values = data['Date']

# Define the y-values (columns to plot) as 'Deaths' and 'Recovered'
y_values = ['Deaths', 'Recovered']

# Define the labels for the legend, and colors for the lines
labels = ['Deaths', 'Recovered']
colors = ['blue', 'green']

# Define the title, x-axis label, y-axis label, and file path to save the plot
title = 'Monthly Deaths and Recovered Cases of Covid-19'
x_label = 'Month'
y_label = 'Count'
save_path = 'monthly_deaths_recovered.png'

# Create a line plot for daily deaths and recovered cases using the defined function
create_line_plot(data, x_values, y_values, labels, colors, title, x_label, y_label, save_path)
