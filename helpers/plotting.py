import matplotlib.pyplot as plt
import seaborn as sns


def plot_categories(df, category, target):
    # Plot a factorplot
    ax = sns.factorplot(category, target, data=df)
    ax.add_legend()

    # Save the figure
    ax.savefig('./figures/%s distribution.png' % category,
               bbox_inches='tight')
