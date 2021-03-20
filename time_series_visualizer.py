import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=[0], index_col=0)
# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) &
            (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    g = df.plot(kind="line")
    g.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    g.set_xlabel("Date")
    g.set_ylabel("Page Views")

    fig = g.figure
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['year'] = [d.year for d in df_bar.date]
    df_bar['month'] = [d.strftime('%B') for d in df_bar.date]

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12, 8))
    ax = sns.barplot(x="year", y="value", hue="month", data=df_bar, ci=None, hue_order=[
                     "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    plot_objects = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
    fig, (ax1, ax2) = plot_objects

    # by year
    # plt.subplot(1,2,1)
    sns.boxplot(ax=ax1, data=df_box, x="year", y="value")
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_ylabel("Page Views")
    ax1.set_xlabel("Year")

    # by month
    sns.boxplot(ax=ax2, data=df_box, x="month", y="value", order=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig


draw_box_plot()
