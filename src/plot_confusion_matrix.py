# Import external libraries
import matplotlib.pyplot as plt
import seaborn as sns

def plot_confusion_matrix(cm):
    fig, ax = plt.subplots(1, 1, figsize=(8,8))
    sns.heatmap(cm, ax=ax, annot=True)
    ax.set_xlabel("predicted")
    ax.set_ylabel("true")