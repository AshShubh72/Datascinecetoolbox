# World Happiness Report 2024 Data Analysis
# Author: [Your Name]
# Objective: Analyze global happiness data to identify patterns, top/bottom countries, and factor correlations

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Objective: Load the dataset
file_path = "F:/College Material/Sem4/Python/Project1/happinesdata.xlsx"
df = pd.read_excel(file_path, sheet_name="Data for Figure 2.1 (2011–2024)")

# Objective: Filter data for the year 2024
df_2024 = df[df["Year"] == 2024]

# Objective: Display column names for reference
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

# ----------------------------- VISUALIZATION PART -----------------------------

# 6. Distribution of Happiness Scores
plt.figure(figsize=(8, 4))
sns.histplot(df_2024["Ladder score"], bins=20, kde=True, color='skyblue')
plt.title("Distribution of Happiness Scores (2024)")
plt.xlabel("Happiness Score")
plt.ylabel("Number of Countries")
plt.tight_layout()
plt.show()

# 7. Correlation Heatmap between Factors
plt.figure(figsize=(12, 8))
sns.heatmap(df_2024.corr(numeric_only=True), annot=True, cmap="YlGnBu", fmt=".2f")
plt.title("Correlation Matrix - Happiness Factors (2024)")
plt.tight_layout()
plt.show()

# 8. Compare Top 5 and Bottom 5 Countries using Barplot
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

# ----------------------------- END OF PROGRAM -----------------------------
