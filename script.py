import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./sales.csv")

#1

online_perc = (df['Sales Channel'].eq('Online').mean()) * 100

#online percantage
print(online_perc)
#offline percantage
print(100-online_perc)

#2

critical_total_in_millions = df.groupby('Order Priority')['Total Profit'].sum()
print(critical_total_in_millions/1e6)


#3

country_max_profit = df.groupby('Country')['Total Profit'].sum().sort_values(ascending=False).head()
print(country_max_profit)

#4

macedonia_df = df[df['Country'].eq('Macedonia')]
macedonia_top_5 = macedonia_df.groupby('Item Type')['Total Profit'].sum().sort_values(ascending=False)
print(macedonia_top_5)

labels = macedonia_top_5.index
sizes = macedonia_top_5.values
colors = plt.cm.Paired(range(len(labels)))  # Color palette

# Calculate percentages for the legend
percentages = [f'{(size / sum(sizes)) * 100:.1f}%' for size in sizes]
legend_labels = [f'{label} - {percent}' for label, percent in zip(labels, percentages)]

# Create the plot
plt.figure(figsize=(14, 8))
plt.pie(sizes, colors=colors, startangle=90)
plt.axis('equal')  # Keeps the pie circular

# Add legend in bottom-left
plt.legend(legend_labels, loc='lower left', bbox_to_anchor=(-0.05, -0.1), fontsize=10, title='Item Types', title_fontsize='13')

plt.title('Top Items by Total Profit in Macedonia')
plt.show()
