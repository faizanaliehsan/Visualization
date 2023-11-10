import pandas as pd
import matplotlib.pyplot as plt

def create_pie_chart(data, labels, colors, title, save_path):
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

# Load the data from the CSV file (replace 'your_data.csv' with your actual file path)
data = pd.read_csv('day_wise.csv')

# Define the labels, colors, and title for the pie chart (excluding "Confirmed")
labels = ['Deaths', 'Recovered', 'Active']
colors = ['red', 'green', 'blue']
title = 'Distribution of Covid-19 Cases'

# Specify the path to save the plot
save_path = 'covid_pie_chart.png'

# Create a pie chart, save it, and display it in your IDE
saved_plot_path = create_pie_chart(data, labels, colors, title, save_path)
