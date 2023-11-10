import pandas as pd
import matplotlib.pyplot as plt

# Load your data from a CSV file or another source
# Replace 'your_data.csv' with the actual file path or data source
data = pd.read_csv('day_wise.csv')

# Add a 15-day gap between the dates
date_column = pd.to_datetime(data['Date'])  # Convert the 'Date' column to a datetime object
date_column += pd.DateOffset(days=15)  # Add a 15-day gap
data['Date'] = date_column  # Update the 'Date' column in the dataset

# Define the columns to be used in the bar chart (excluding 'Deaths / 100 Cases')
columns = ['Recovered / 100 Cases', 'Deaths / 100 Recovered']

# Define the labels and colors for the chart
labels = data['Date']  # Replace 'Date' with the column representing time periods or regions
colors = ['green', 'blue']  # Adjust colors accordingly

# Create a percentage stacked bar chart without 'Deaths / 100 Cases'
plt.figure(figsize=(10, 6))
plt.bar(labels, data['Recovered / 100 Cases'], color=colors[0], label='Recovered / 100 Cases', alpha=0.7)
plt.bar(labels, data['Deaths / 100 Recovered'], color=colors[1], label='Deaths / 100 Recovered', alpha=0.7)

# Set labels and title
plt.xlabel('Months')
plt.ylabel('Percentage (%)')
plt.title('Comparison of COVID-19 Fatality and Recovery Rates Over Time')

# Add a legend
plt.legend()

# Show the bar chart
plt.tight_layout()
plt.show()

# Define a function to create a pie chart (which is not used in this code)
def create_bar_chart(data, labels, colors, title, save_path):
    total_values = [data[label].sum() for label in labels]

    plt.figure(figsize=(8, 8))
    plt.pie(total_values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

    plt.title(title)

    plt.axis('equal')

    # Save the plot to a file
    plt.savefig(save_path)

    # Display the plot in your IDE
    plt.show()
    
    # Close the plot to release memory
    plt.close()

    return save_path  # Return the path of the saved plot
