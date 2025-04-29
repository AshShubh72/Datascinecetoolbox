# My 2024 Happiness Data Code

# Need these for data and graphs
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load my Excel file
file = "F:/College Material/Sem4/Python/Project1/happinesdata.xlsx"
data = pd.read_excel(file, sheet_name="Data for Figure 2.1 (2011–2024)")

# Get only 2024 data
data_2024 = data[data["Year"] == 2024]

# Objective 1: Show all columns
print("Columns in my data:")
print(data_2024.columns.tolist())

# ### MAIN OBJECTIVE 1 ###: Top 10 happiest countries
print("\nTop 10 Happy Countries:")
happy = data_2024[["Country name", "Ladder score"]].sort_values(by="Ladder score", ascending=False).head(10)
print(happy)

# ### MAIN OBJECTIVE 2 ###: Bottom 10 least happy countries
print("\nBottom 10 Sad Countries:")
sad = data_2024[["Country name", "Ladder score"]].sort_values(by="Ladder score").head(10)
print(sad)

# ### MAIN OBJECTIVE 3 ###: Top 10 countries by GDP
print("\nTop 10 Countries by GDP:")
rich = data_2024[["Country name", "Explained by: Log GDP per capita"]].sort_values(by="Explained by: Log GDP per capita", ascending=False).head(10)
print(rich)

# ### MAIN OBJECTIVE 4 ###: Highest and lowest life expectancy
high_life = data_2024.loc[data_2024["Explained by: Healthy life expectancy"].idxmax()]
low_life = data_2024.loc[data_2024["Explained by: Healthy life expectancy"].idxmin()]
print(f"\nHighest Life Expectancy: {high_life['Country name']} ({high_life['Explained by: Healthy life expectancy']})")
print(f"Lowest Life Expectancy: {low_life['Country name']} ({low_life['Explained by: Healthy life expectancy']})")

# ### MAIN OBJECTIVE 5 ###: Bar graph for top 5 and bottom 5 countries
top_5 = happy.head(5)
bottom_5 = sad.head(5)
both = pd.concat([top_5, bottom_5])
plt.figure()
sns.barplot(x="Ladder score", y="Country name", data=both, color="lightblue")
plt.title("Happy vs Sad Countries")
plt.xlabel("Happiness Score")
plt.ylabel("Country")
plt.show()

# ### MAIN OBJECTIVE 6 ###: Heatmap for connections
plt.figure()
sns.heatmap(data_2024.corr(numeric_only=True), annot=True, cmap="cool")
plt.title("How Stuff Connects")
plt.show()

# Objective 7: Pie chart for what makes happiness
factors = [
    "Explained by: Log GDP per capita",
    "Explained by: Social support",
    "Explained by: Healthy life expectancy",
    "Explained by: Freedom to make life choices",
    "Explained by: Generosity",
    "Explained by: Perceptions of corruption"
]
avg = data_2024[factors].mean()
plt.figure()
plt.pie(avg, labels=[name.replace("Explained by: ", "") for name in avg.index], autopct="%1.1f%%", colors=sns.color_palette("pastel"))
plt.title("What Makes Happiness")
plt.show()

# Objective 8: Top 10 countries by social support
print("\nTop 10 Countries by Social Support:")
support = data_2024[["Country name", "Explained by: Social support"]].sort_values(by="Explained by: Social support", ascending=False).head(10)
print(support)

# Objective 9: Scatter plot for GDP vs happiness
plt.figure()
sns.scatterplot(data=data_2024, x="Explained by: Log GDP per capita", y="Ladder score")
plt.title("Money vs Happiness")
plt.xlabel("GDP")
plt.ylabel("Happiness Score")
plt.show()

print("\nAll done! I made graphs, a heatmap, and a pie chart!")
