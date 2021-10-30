import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Function to plot the distributions of a series data_count
def plot_distribution(counts):
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    sns.barplot(y=counts.values, x=counts.index, ax=ax)
    sns.despine(left=True)
    ax.set_ylabel("Frequeny")
    ax.set_xlabel(counts.name)
    ax.set_title("Distribution")
    plt.xticks(rotation=90, ha='right')
    plt.show()