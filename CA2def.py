# World Happiness Report 2024 Data Analysis

# Objective: Analyze global happiness data to identify patterns, top/bottom countries, and factor correlations

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Objective: Load the dataset from the World Happiness Report 2024 Excel file
file_path = "F:/College Material/Sem4/Python/Project1/happinesdata.xlsx"
df = pd.read_excel(file_path, sheet_name="Data for Figure 2.1 (2011–2024)")

# Objective: Extract data specific to the year 2024 for focused analysis
df_2024 = df[df["Year"] == 2024]

# Objective: Display column names to understand available variables for analysis
print("Available Columns:\n", df_2024.columns.tolist())

# ----------------------------- ANALYSIS PART -----------------------------

# 1. Top 10 Happiest Countries
print("\nTop 10 Happiest Countries in 2024:")
print(df_2024[["Country name", "Ladder score"]].sort_values(by="Ladder score", ascending=False).head(10))

# 2. Bottom 10 Least Happy Countries
print("\nBottom 10 Least Happy Countries in 2024:")
print(df_2024[["Country name", "Ladder score"]].sort_values(by="Ladder score").head(10))

# 3. Top 10 Countries by GDP per Capita
print("\nTop 10 Countries by GDP per Capita in 2024:")
print(df_2024[["Country name", "Explained by: Log GDP per capita"]].sort_values(by="Explained by: Log GDP per capita", ascending=False).head(10))

# 4. Top 10 Countries by Social Support
print("\nTop 10 Countries by Social Support in 2024:")
print(df_2024[["Country name", "Explained by: Social support"]].sort_values(by="Explained by: Social support", ascending=False).head(10))

# 5. Top 10 Countries by Perception of Corruption
print("\nTop 10 Countries by Perception of Corruption (Higher = Worse) in 2024:")
print(df_2024[["Country name", "Explained by: Perceptions of corruption"]].sort_values(by="Explained by: Perceptions of corruption", ascending=False).head(10))

# 6. Top 10 Countries by Freedom to Make Life Choices
print("\nTop 10 Countries by Freedom in 2024:")
print(df_2024[["Country name", "Explained by: Freedom to make life choices"]].sort_values(
    by="Explained by: Freedom to make life choices", ascending=False).head(10))

# 7. Country with Highest & Lowest Healthy Life Expectancy
highest_life = df_2024.loc[df_2024["Explained by: Healthy life expectancy"].idxmax()]
lowest_life = df_2024.loc[df_2024["Explained by: Healthy life expectancy"].idxmin()]

print(f"\nCountry with Highest Healthy Life Expectancy: {highest_life['Country name']} ({highest_life['Explained by: Healthy life expectancy']})")
print(f"Country with Lowest Healthy Life Expectancy: {lowest_life['Country name']} ({lowest_life['Explained by: Healthy life expectancy']})")

# 8. Save filtered 2024 data to CSV
df_2024.to_csv("happiness_2024_filtered.csv", index=False)
print("\nFiltered 2024 data saved as 'happiness_2024_filtered.csv'")

# ----------------------------- VISUALIZATION PART -----------------------------

# 9. Distribution of Happiness Scores
plt.figure(figsize=(8, 4))
sns.histplot(df_2024["Ladder score"], bins=20, kde=True, color='skyblue')
plt.title("Distribution of Happiness Scores (2024)")
plt.xlabel("Happiness Score")
plt.ylabel("Number of Countries")
plt.tight_layout()
plt.show()

# 10. Correlation Heatmap between Factors
plt.figure(figsize=(12, 8))
sns.heatmap(df_2024.corr(numeric_only=True), annot=True, cmap="YlGnBu", fmt=".2f")
plt.title("Correlation Matrix - Happiness Factors (2024)")
plt.tight_layout()
plt.show()

# 11. Compare Top 5 and Bottom 5 Countries using Barplot
top5 = df_2024.sort_values(by="Ladder score", ascending=False).head(5)
bottom5 = df_2024.sort_values(by="Ladder score").head(5)
compare = pd.concat([top5, bottom5])

plt.figure(figsize=(10, 6))
sns.barplot(x="Ladder score", y="Country name", data=compare, palette="coolwarm")
plt.title("Top 5 vs Bottom 5 Happiest Countries (2024)")
plt.xlabel("Happiness Score")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

# 12. Factor Contribution to Happiness in Top 10 Countries
top10 = df_2024.sort_values(by="Ladder score", ascending=False).head(10)
factors = [
    "Explained by: Log GDP per capita",
    "Explained by: Social support",
    "Explained by: Healthy life expectancy",
    "Explained by: Freedom to make life choices",
    "Explained by: Generosity",
    "Explained by: Perceptions of corruption"
]
top10_factors = top10[["Country name"] + factors].set_index("Country name")

top10_factors.plot(kind='bar', stacked=True, figsize=(12, 6), colormap="tab20")
plt.title("Factor Contributions to Happiness - Top 10 Countries (2024)")
plt.ylabel("Contribution Value")
plt.xlabel("Country")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 13. Scatter Plot: GDP vs Happiness
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df_2024, x="Explained by: Log GDP per capita", y="Ladder score", hue="Country name", legend=False)
plt.title("Relationship Between GDP and Happiness Score (2024)")
plt.xlabel("Log GDP per Capita")
plt.ylabel("Happiness Score")
plt.tight_layout()
plt.show()

# 14. Pie Chart: Average Factor Contributions
avg_factors = df_2024[factors].mean()
plt.figure(figsize=(8, 8))
plt.pie(avg_factors, labels=avg_factors.index.str.replace("Explained by: ", ""), autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title("Average Contribution of Happiness Factors (2024)")
plt.axis('equal')
plt.tight_layout()
plt.show()

# ----------------------------- END OF PROGRAM -----------------------------
